import psycopg2
from psycopg2.extras import RealDictCursor
from app.config import settings
import time

def get_db_connection():
    """Tenta conectar ao PostgreSQL com retentativas."""
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(settings.DATABASE_URL, cursor_factory=RealDictCursor)
            return conn
        except Exception as e:
            print(f"Erro ao conectar ao banco (restam {retries} tentativas): {e}")
            retries -= 1
            time.sleep(2)
    return None

def init_db():
    """Cria a tabela video_jobs se não existir."""
    conn = get_db_connection()
    if not conn:
        print("Falha crítica: Não foi possível conectar ao banco para inicializar.")
        return

    try:
        with conn.cursor() as cur:
            # 1. Cria tabela base (para instalações novas)
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
                    
                    -- Novos campos SEO/Expansão
                    formato TEXT,       -- 'shorts', 'video_longo', 'reels'
                    regiao TEXT,        -- 'BR', 'Global', 'Latam'
                    agregacao TEXT,     -- Tag de agrupamento ex: 'digest_morning'
                    pub_date TIMESTAMP WITH TIME ZONE, -- Data de agendamento/publicação
                    published BOOLEAN DEFAULT FALSE,
                    metadata_post JSONB DEFAULT '{}', -- Dados para redes sociais (tags, hashtags, desc)
                    platform_id TEXT,   -- ID do vídeo na plataforma (ex: YouTube ID)
                    metrics JSONB DEFAULT '{}', -- Analytics (views, likes, ctr, retention)

                    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                );
            """)
            conn.commit()
            
            # 2. Migração automática (para tabelas existentes)
            
            alter_commands = [
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS formato TEXT;",
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS regiao TEXT;",
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS agregacao TEXT;",
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS pub_date TIMESTAMP WITH TIME ZONE;",
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS published BOOLEAN DEFAULT FALSE;",
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS metadata_post JSONB DEFAULT '{}';",
                # Convenience generated columns (avoid manual JSONB extraction in queries)
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS youtube_id TEXT GENERATED ALWAYS AS ((metadata_post->>'youtube_id')) STORED;",
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS tiktok_id TEXT GENERATED ALWAYS AS ((metadata_post->>'tiktok_id')) STORED;",
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS platform_id TEXT;",
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS metrics JSONB DEFAULT '{}';",
                "ALTER TABLE video_jobs ADD COLUMN IF NOT EXISTS error_message TEXT;"
            ]
            
            for cmd in alter_commands:
                try:
                    cur.execute(cmd)
                    conn.commit()
                except Exception as ex_alter:
                    print(f"Nota de Migração: {ex_alter}")
                    conn.rollback() 
                    # Importante: rollback apenas do comando atual para continuar
                    
            conn.commit()
            print("Tabela video_jobs verificada e migrada com sucesso.")
            
    except Exception as e:
        print(f"Erro ao inicializar banco: {e}")
    finally:
        conn.close()
