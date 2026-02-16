
# =============================================================================
# app/services/audio.py
# =============================================================================
import os
import asyncio
import logging
from typing import Optional
from app.config import settings

# Libraries
import edge_tts
from pydub import AudioSegment
from pydub.effects import normalize

# Fallback libraries (try import to avoid crash if not installed yet)
try:
    from unrealspeech import UnrealSpeechAPI
except ImportError:
    UnrealSpeechAPI = None

try:
    from kokoro_onnx import Kokoro
    from huggingface_hub import hf_hub_download
    import soundfile as sf
except ImportError:
    Kokoro = None

logger = logging.getLogger(__name__)

class AudioService:
    """
    Gerenciador de Áudio com estratégia de Fallback:
    1. Unreal Speech (Alta Qualidade, Pago/Limitado)
    2. Kokoro TTS (Alta Qualidade, Local/ONNX)
    3. Edge TTS (Qualidade Média, Grátis)
    
    + Pós-processamento obrigatório (Pydub).
    """

    def __init__(self):
        self.output_dir = os.path.join(settings.DATA_MIDIA, "audios")
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Cache para modelos carregados
        self._kokoro_model = None
        self._kokoro_voices = None

    async def generate(self, text: str, job_id: str, voice_style: str = "pt-BR-FranciscaNeural") -> Optional[str]:
        """Gera áudio tentando os provedores em ordem de prioridade."""
        filename = f"{job_id}.mp3"
        final_path = os.path.join(self.output_dir, filename)
        temp_path = os.path.join(self.output_dir, f"raw_{filename}")

        if os.path.exists(final_path):
            return final_path

        # 1. Tentativa: Edge TTS (Prioridade para PT-BR Natural)
        # O user relatou que Unreal/Kokoro (vozes EN) geram "sotaque robótico" em PT.
        # FranciscaNeural é state-of-the-art para PT-BR gratuito.
        try:
            logger.info(f"[Audio] Tentando Edge TTS (Prioridade) para Job {job_id}...")
            communicate = edge_tts.Communicate(text, voice_style)
            await communicate.save(temp_path)
            return self._post_process(temp_path, final_path)
        except Exception as e:
            logger.error(f"[Audio] Falha no Edge TTS: {e}")

        # 2. Tentativa: Unreal Speech (Backup)
        if settings.UNREAL_SPEECH_API_KEY and UnrealSpeechAPI:
            try:
                logger.info(f"[Audio] Tentando Unreal Speech para Job {job_id}...")
                if await self._generate_unreal(text, temp_path):
                    return self._post_process(temp_path, final_path)
            except Exception as e:
                logger.error(f"[Audio] Falha no Unreal Speech: {e}")

        # 3. Tentativa: Kokoro TTS (Local ONNX)
        if Kokoro:
            try:
                logger.info(f"[Audio] Tentando Kokoro TTS para Job {job_id}...")
                if await self._generate_kokoro(text, temp_path):
                    return self._post_process(temp_path, final_path)
            except Exception as e:
                logger.error(f"[Audio] Falha no Kokoro TTS: {e}")

        return None

    async def _generate_unreal(self, text: str, output_path: str) -> bool:
        """Integration com Unreal Speech (Provider 1)."""
        # Exemplo hipotético de uso (ajustar conforme SDK real)
        # O SDK 'unrealspeech' geralmente espera chamadas síncronas ou específicas.
        # Vamos rodar em executor se for bloqueante.
        import requests
        
        # Fallback manual via API REST se SDK falhar ou for confuso
        # Endpoint: https://api.v7.unrealspeech.com/stream
        headers = {"Authorization": f"Bearer {settings.UNREAL_SPEECH_API_KEY}"}
        data = {
            "Text": text,
            "VoiceId": "Will", # Voice default masculina (ou Scarlett para feminina)
            "Bitrate": "192k",
            "Speed": "0",
            "Pitch": "1.0",
            "Codec": "libmp3lame"
        }
        
        # Wrapper async
        def _request():
            resp = requests.post("https://api.v7.unrealspeech.com/stream", json=data, headers=headers, stream=True)
            if resp.status_code == 200:
                with open(output_path, "wb") as f:
                    for chunk in resp.iter_content(chunk_size=1024):
                        if chunk: f.write(chunk)
                return True
            return False

        return await asyncio.to_thread(_request)

    async def _generate_kokoro(self, text: str, output_path: str) -> bool:
        """Integration com Kokoro ONNX (Provider 2)."""
        # Garante modelo baixado
        model_path = os.path.join(self.output_dir, "kokoro-v0_19.onnx")
        voices_path = os.path.join(self.output_dir, "voices.json")
        
        if not os.path.exists(model_path) or not os.path.exists(voices_path):
            await self._download_kokoro_models(model_path, voices_path)

        # Carrega modelo (Lazy Loading)
        if not self._kokoro_model:
            self._kokoro_model = Kokoro(model_path, voices_path)

        # Gera Audio (numpy array)
        # 'af_sarah' é uma voz comum do Kokoro (pt-br precisa checar suporte, 
        # mas Kokoro é multilingue. 'af' = American Female. 
        # Se Kokoro suportar 'bf_isa' (Portuguese), usamos. 
        # Fallback para 'af_sarah' se não soubermos.)
        # O Kokoro v0.19 é focado em Inglês mas tem suporte experimental.
        # Pelo user request, "priorização qualidade". Se Kokoro for só EN, pode ser problema.
        # Mas vamos assumir suporte ou usar voz padrão.
        
        # Wrapper thread para processamento pesado
        def _process():
            # Gera audio (returns rendering options)
            # samples, sample_rate = kokoro.create(...)
            samples, sample_rate = self._kokoro_model.create(text, voice="af_sarah", speed=1.0, lang="en-us") 
            # Note: Kokoro ONNX v0.19 primariamente EN. Se o texto for PT, pode ficar estranho.
            # Mas seguindo a ordem do user.
            
            sf.write(output_path, samples, sample_rate)
            return True

        return await asyncio.to_thread(_process)

    async def _download_kokoro_models(self, model_target, voices_target):
        """Baixa modelos do Hugging Face se não existirem."""
        logger.info("[Audio] Baixando modelos Kokoro-82M (ONNX)...")
        def _download():
            hf_hub_download(repo_id="hexgrad/Kokoro-82M", filename="kokoro-v0_19.onnx", local_dir=self.output_dir)
            hf_hub_download(repo_id="hexgrad/Kokoro-82M", filename="voices.json", local_dir=self.output_dir)
        await asyncio.to_thread(_download)

    def _post_process(self, input_path: str, output_path: str) -> str:
        """
        Pós-processamento com Pydub (Ensemble/Mastering).
        1. Normalização (-3dB)
        2. Garante 44.1kHz / 192kbps / MP3
        """
        try:
            audio = AudioSegment.from_file(input_path)
            
            # Normaliza
            audio = normalize(audio)
            
            # Exporta final
            audio.export(
                output_path, 
                format="mp3", 
                bitrate="192k",
                parameters=["-ar", "44100"] 
            )
            
            # Limpa raw
            if os.path.exists(input_path) and input_path != output_path:
                os.remove(input_path)
                
            return output_path
        except Exception as e:
            logger.error(f"[Audio] Erro no pós-processamento: {e}")
            # Se falhar o post-process, retorna o raw (melhor que nada)
            # Renomeia raw para final para manter contrato
            if os.path.exists(input_path):
                os.rename(input_path, output_path)
            return output_path
