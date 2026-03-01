# =============================================================================
# app/services/audio.py — Serviço Interno de Geração de Áudio (TTS)
# =============================================================================
#
# Este módulo é a "camada base" do áudio: é chamado diretamente pelo
# video_engine.py durante o processamento de vídeo.
#
# COMO O SSML FUNCIONA:
#   SSML (Speech Synthesis Markup Language) é uma linguagem XML que instrui
#   o sintetizador de voz sobre COMO falar, não apenas O QUE falar.
#   Exemplos de efeitos:
#     - <emphasis level="strong">ABSURDO</emphasis> → fala enfatizada
#     - <break time="400ms"/>  → pausa de 0.4 segundos
#     - <prosody rate="fast">  → fala mais rápida para CTA/urgência
#
#   O edge-tts suporta SSML nativamente via Communicate(ssml=True).
#   Isso melhora significativamente o engajamento do vídeo, pois a narração
#   soa mais humana e dinâmica.
#
# MOTIVAÇÃO DO LOGGING vs PRINT:
#   print() vai para stdout sem timestamp nem nível de severidade.
#   logging.getLogger() permite filtrar por nível (INFO, WARNING, ERROR)
#   e aparece no Dozzle com contexto: [19:35:00][audio_service] INFO: ...
# =============================================================================

import os
import re
import asyncio
import logging
import edge_tts
from app.config import settings

# Logger específico para este módulo
logger = logging.getLogger("audio_service")


class AudioService:
    """
    Serviço de Text-to-Speech usando Microsoft Edge TTS (gratuito, sem API key).

    Suporta SSML para ênfase emocional automática na narração de futebol.
    """

    # Vozes e Personas (v13 Diversificação)
    # Antonio: Clássica/Grave (Raiz)
    # Francisca: Formal/Pro (Analítico)
    # Thalita: Energética/Aguda (Fanático)
    VOICES = {
        "news": "pt-BR-AntonioNeural",
        "shorts": "pt-BR-AntonioNeural",
        "urgent": "pt-BR-FranciscaNeural",
        # Personas Específicas
        "raiz": "pt-BR-AntonioNeural",
        "analitico": "pt-BR-FranciscaNeural",
        "fanatico": "pt-BR-ThalitaNeural",
    }

    def __init__(self):
        self.default_voice = "pt-BR-AntonioNeural"
        self.output_dir = os.path.join(settings.DATA_MIDIA, "audios")
        os.makedirs(self.output_dir, exist_ok=True)

    def clean_text(self, text: str) -> str:
        """
        Remove elementos que quebram o TTS: URLs, markdown, emojis problemáticos.

        Nota: NÃO remove acentos (encode ascii) pois o português precisa deles.
        """
        if not text:
            return ""
        # Remove URLs completas (http:// ou https://)
        text = re.sub(r"http\S+", "", text)
        # Remove formatação Markdown: *bold*, _italic_, **negrito**
        text = re.sub(r"[*_]{1,2}([^*_]+)[*_]{1,2}", r"\1", text)
        # Remove espaços extras e quebras múltiplas
        text = re.sub(r"\s+", " ", text).strip()
        return text

    def build_ssml(self, text: str, style: str = "news") -> str:
        """
        Converte texto limpo em SSML para narração mais expressiva.

        O SSML é um padrão W3C suportado pelo edge-tts. Ele permite controlar:
          - Ênfase em palavras (<emphasis>)
          - Pausas entre frases (<break>)
          - Velocidade e tom (<prosody>)

        ALGORITMO:
          1. Remove qualquer tag XML existente (evita duplicação)
          2. Envolve palavras em CAPS com <emphasis level="strong">
             → ex: "ABSURDO" → "<emphasis level='strong'>ABSURDO</emphasis>"
          3. Adiciona <break> após pontuação (ponto, vírgula, reticências)
          4. Aplica <prosody rate=...> baseado no estilo do vídeo
          5. Envolve tudo no envelope <speak> XML obrigatório

        Args:
            text:  Texto já limpo (sem URLs, markdown)
            style: "news" | "shorts" | "urgent" — define velocidade

        Returns:
            String SSML válida para Communicate(ssml=True) do edge-tts
        """
        # Passo 1: Remove tags SSML existentes (proteção contra duplicação)
        text = re.sub(r"<[^>]+>", "", text)

        # Passo 2: Define velocidade e pitch por estilo
        # "fast" acelera a dicção para Shorts — TikTok tem audiência acelerada
        # "+8%" aumenta o pitch para urgência — soa mais alarmante
        rate_map = {"shorts": "fast", "urgent": "+10%", "news": "+0%"}
        pitch_map = {"shorts": "+3%", "urgent": "+8%", "news": "+0%"}
        rate = rate_map.get(style, "+0%")
        pitch = pitch_map.get(style, "+0%")

        # Passo 3: Adiciona pausas APÓS pontuação e [PAUSA] ANTES do emphasize
        # Pontos finais: 350ms — pausa natural entre frases
        # Vírgulas: 150ms — micro-pausa para respiração
        # Reticências: 500ms — efeito de suspense
        # Marcação explícita da IA [PAUSA]: 300ms
        text = re.sub(r"\[PAUSA\]", '<break time="300ms"/>', text)
        text = re.sub(r"\.", '.<break time="350ms"/>', text)
        text = re.sub(r",", ',<break time="150ms"/>', text)
        text = re.sub(r";", ';<break time="200ms"/>', text)
        text = re.sub(r"\.\.\.", '...<break time="500ms"/>', text)

        # Passo 4: Adiciona ênfase em palavras CAPS (≥ 3 letras)
        # Regex: \b = palavra inteira, [A-ZÁÉÍÓÚÂÊÔÃÕÇ]{3,} = letras maiúsculas (incluindo acentos BR)
        def emphasize(match):
            word = match.group(0)
            return f'<emphasis level="strong">{word}</emphasis>'

        text = re.sub(r"\b[A-ZÁÉÍÓÚÂÊÔÃÕÇ]{3,}\b", emphasize, text)

        # Passo 5: Monta o envelope SSML obrigatório
        # <speak> com namespace W3C é OBRIGATÓRIO para o edge-tts reconhecer como SSML
        # xml:lang garante que a pronúncia use as regras fonéticas do português BR
        ssml = (
            f'<speak xmlns="http://www.w3.org/2001/10/synthesis" '
            f'xml:lang="pt-BR">\n'
            f'  <prosody rate="{rate}" pitch="{pitch}">\n'
            f"    {text}\n"
            f"  </prosody>\n"
            f"</speak>"
        )
        return ssml

    async def generate(self, text: str, job_id: str, style: str = "news") -> str:
        """
        Gera áudio MP3 a partir do texto usando Edge TTS com SSML.

        FLUXO:
          1. Limpa o texto (remove URLs, markdown)
          2. Converte para SSML com ênfase automática
          3. Chama edge-tts com ssml=True
          4. Salva como MP3 em output_dir/job_id.mp3

        Args:
            text:    Texto do roteiro
            job_id:  UUID do job (usado como nome do arquivo)
            style:   Estilo de narração: "news" | "shorts" | "urgent"

        Returns:
            Path absoluto do arquivo MP3 gerado.

        Raises:
            RuntimeError se o arquivo não for gerado.
        """
        clean = self.clean_text(text)
        if not clean:
            logger.warning("[AudioService] Texto vazio para job %s — áudio não gerado", job_id)
            return ""

        output_path = os.path.join(self.output_dir, f"{job_id}.mp3")

        # Seleciona a voz baseada no estilo
        voice = self.VOICES.get(style, self.default_voice)

        # Gera SSML para narração mais expressiva
        ssml = self.build_ssml(clean, style=style)
        logger.info("[AudioService] Gerando áudio SSML | job=%s | voice=%s | style=%s", job_id, voice, style)

        try:
            # edge-tts: Communicate com ssml=True processa as tags SSML
            # Em vez de falar "ponto-e-vírgula", o TTS pausa o tempo certo
            communicate = edge_tts.Communicate(ssml, voice, ssml=True)
            await communicate.save(output_path)

            if os.path.exists(output_path) and os.path.getsize(output_path) > 1024:
                # Verifica tamanho mínimo (1 KB) para detectar falhas silenciosas
                size_kb = os.path.getsize(output_path) / 1024
                logger.info("[AudioService] Áudio gerado: %s (%.1f KB)", output_path, size_kb)
                return output_path
            else:
                raise RuntimeError(f"Arquivo de áudio não encontrado ou vazio: {output_path}")

        except Exception as e:
            logger.error("[AudioService] Erro ao gerar áudio SSML para job %s: %s", job_id, e)
            # Fallback: tenta sem SSML (texto simples)
            try:
                logger.warning("[AudioService] Tentando fallback sem SSML para job %s", job_id)
                communicate_plain = edge_tts.Communicate(clean, voice)
                await communicate_plain.save(output_path)
                if os.path.exists(output_path):
                    logger.info("[AudioService] Fallback sem SSML OK: %s", output_path)
                    return output_path
            except Exception as e2:
                logger.error("[AudioService] Fallback também falhou: %s", e2)
            raise e
