# =============================================================================
# app/utils/database.py — Conexão e Inicialização do PostgreSQL
# =============================================================================
#
# REGRA DE OURO DE MIGRAÇÃO:
#   Nunca usamos DROP ou ALTER sem IF NOT EXISTS / IF EXISTS.
#   Isso garante que instalações existentes em produção não quebrem.
#
# LOGGING vs PRINT:
#   Substituímos todos os print() por logging.getLogger() para que as
#   mensagens apareçam corretamente no Dozzle (sistema de observação de logs
#   em Docker). O 'print' vai para stdout sem timestamp; o 'logging' adiciona
#   nível e contexto, facilitando o diagnóstico.
# =============================================================================

import psycopg2
from psycopg2.extras import RealDictCursor
from app.config import settings
import time
import logging

# Cria um logger específico para este módulo.
# O nome "database" aparecerá nos logs do Dozzle ao lado de cada mensagem.
logger = logging.getLogger("database")


def get_db_connection():
    """
    Tenta conectar ao PostgreSQL com 5 tentativas e 2s de espera entre elas.

    Retorna:
        conn — objeto de conexão psycopg2 com RealDictCursor ativado
               (permite acessar colunas por nome: row['title'] ao invés de row[0])
        None — se todas as tentativas falharem (ex: Postgres ainda subindo)
    """
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(settings.DATABASE_URL, cursor_factory=RealDictCursor)
            return conn
        except Exception as e:
            # INFO aqui pois é esperado durante o boot do Docker (Postgres pode demorar)
            logger.info("Erro ao conectar ao banco (restam %d tentativas): %s", retries, e)
            retries -= 1
            time.sleep(2)
    return None


def init_db():
    """
    Cria e migra a tabela video_jobs com segurança para produção.

    Esta função é chamada uma vez no boot do python_service (app/main.py).
    Ela usa dois blocos:

    1. CREATE TABLE IF NOT EXISTS — cria a tabela pela primeira vez em instalações novas.
    2. ALTER TABLE ... ADD COLUMN IF NOT EXISTS — adiciona colunas em instalações existentes
       sem derrubar os dados já gravados.

    Cada ALTER é executado em seu próprio bloco try/except + rollback para que
    um erro em uma coluna não bloqueie a migração das outras.
    """
    conn = get_db_connection()
    if not conn:
        logger.error("Falha crítica: não foi possível conectar ao banco para inicializar.")
        return

    try:
        with conn.cursor() as cur:

            # ------------------------------------------------------------------
            # BLOCO 1 — CRIAÇÃO DA TABELA BASE (instalações novas)
            # ------------------------------------------------------------------
            # IF NOT EXISTS garante que esta instrução é idempotente:
            # pode ser executada milhares de vezes sem erro.
            cur.execute("""
                CREATE TABLE IF NOT EXISTS video_jobs (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    source_url TEXT NOT NULL,
                    title TEXT,
                    status TEXT DEFAULT 'pending',
                    category TEXT,
                    priority TEXT DEFAULT 'normal',
                    audio_path TEXT,
                    video_path TEXT,
                    thumbnail_path TEXT,
                    metadata JSONB DEFAULT '{}',
                    retry_count INTEGER DEFAULT 0,
                    error_message TEXT,

                    -- Campos SEO / Multi-plataforma
                    formato TEXT,           -- 'shorts', 'video_longo', 'reels'
                    regiao TEXT,            -- 'BR', 'Global', 'Latam'
                    agregacao TEXT,         -- Tag de agrupamento ex: 'digest_morning'
                    pub_date TIMESTAMP WITH TIME ZONE,
                    published BOOLEAN DEFAULT FALSE,
                    metadata_post JSONB DEFAULT '{}', -- Dados para redes sociais
                    platform_id TEXT,       -- ID do vídeo na plataforma (ex: YouTube ID)
                    metrics JSONB DEFAULT '{}', -- Analytics (views, likes, ctr, retention)

                    -- Campo de log de IA (Etapa 1 — FASE 1)
                    -- Armazena o payload completo enviado ao LLM e a resposta recebida.
                    -- Tipo JSONB permite consultas avançadas: ex: WHERE ai_log->>'model' = 'llama3.3'
                    ai_log JSONB DEFAULT '{}',

                    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                );
            """)
            conn.commit()

            # ------------------------------------------------------------------
            # BLOCO 2 — MIGRAÇÃO INCREMENTAL (instalações existentes)
            # ------------------------------------------------------------------
            # ADD COLUMN IF NOT EXISTS: adicionado no PostgreSQL 9.6+.
            # Cada comando é independente: se um falhar (coluna já existe com
            # tipo diferente, por exemplo), damos rollback só daquele comando
            # e continuamos os próximos.
            alter_commands = [
                # Colunas de controle de publicação
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS formato TEXT;",
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS regiao TEXT;",
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS agregacao TEXT;",
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS pub_date TIMESTAMP WITH TIME ZONE;",
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS published BOOLEAN DEFAULT FALSE;",
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS metadata_post JSONB DEFAULT '{}';",
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS platform_id TEXT;",
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS metrics JSONB DEFAULT '{}';",
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS error_message TEXT;",
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS retry_count INTEGER DEFAULT 0;",

                # Colunas geradas automaticamente (computed columns PostgreSQL 12+)
                # Extraem youtube_id e tiktok_id do JSONB metadata_post para
                # buscas SQL mais rápidas sem precisar usar o operador ->>
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS youtube_id TEXT GENERATED ALWAYS AS ((metadata_post->>'youtube_id')) STORED;",
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS tiktok_id TEXT GENERATED ALWAYS AS ((metadata_post->>'tiktok_id')) STORED;",

                # NOVA COLUNA — Etapa 1, FASE 1
                # ai_log armazena: model, prompt enviado, resposta recebida,
                # latência e status. Serve para auditar e reprocessar chamadas
                # ao LLM sem depender de logs externos.
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS ai_log JSONB DEFAULT '{}';",

                # NOVA COLUNA — horário de publicação agendada
                # Armazena o ISO 8601 UTC do próximo horário de pico calculado
                # pela função get_peak_hours_schedule() em publish.py.
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS scheduled_at TEXT;",
            ]

            for cmd in alter_commands:
                try:
                    cur.execute(cmd)
                    conn.commit()
                except Exception as ex_alter:
                    # Nível INFO pois geralmente indica coluna já existente —
                    # não é um erro grave, é comportamento esperado em re-deploys.
                    logger.info("Migração (esperado em re-deploys): %s", ex_alter)
                    conn.rollback()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS news_leads (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    title TEXT NOT NULL,
                    url TEXT UNIQUE NOT NULL,
                    content TEXT,
                    source TEXT,
                    language TEXT DEFAULT 'pt',
                    status TEXT DEFAULT 'pending',
                    metadata JSONB DEFAULT '{}',
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                );
            """)

            conn.commit()
            logger.info("Tabela video_jobs e news_leads verificadas/migradas.")

    except Exception as e:
        logger.error("Erro ao inicializar banco: %s", e)
    finally:
        conn.close()
