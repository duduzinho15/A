
# =============================================================================
# app/services/subtitles.py
# =============================================================================
import os
import math
import logging
from faster_whisper import WhisperModel

logger = logging.getLogger(__name__)

class SubtitleService:
    def __init__(self, model_size="tiny", device="cpu", compute_type="int8"):
        """
        Inicializa o modelo Whisper.
        model_size: tiny, base, small, medium, large-v2
        device: cpu ou cuda
        """
        self.model_size = model_size
        self.device = device
        self.compute_type = compute_type
        self._model = None

    @property
    def model(self):
        if self._model is None:
            logger.info(f"[Subtitles] Carregando modelo Whisper '{self.model_size}'...")
            self._model = WhisperModel(self.model_size, device=self.device, compute_type=self.compute_type)
        return self._model

    def generate_srt(self, audio_path: str, output_srt_path: str):
        """Transcreve áudio e salva em formato SRT."""
        try:
            logger.info(f"[Subtitles] Transcrevendo {audio_path}...")
            segments, info = self.model.transcribe(audio_path, beam_size=5, language="pt")
            
            with open(output_srt_path, "w", encoding="utf-8") as f:
                for i, segment in enumerate(segments, start=1):
                    start = self._format_timestamp(segment.start)
                    end = self._format_timestamp(segment.end)
                    text = segment.text.strip()
                    
                    f.write(f"{i}\n")
                    f.write(f"{start} --> {end}\n")
                    f.write(f"{text}\n\n")
            
            logger.info(f"[Subtitles] SRT salvo em {output_srt_path}")
            return output_srt_path
        except Exception as e:
            logger.error(f"[Subtitles] Erro ao gerar legendas: {e}")
            return None

    def _format_timestamp(self, seconds: float):
        """Converte segundos para formato SRT (HH:MM:SS,mmm)."""
        hours = math.floor(seconds / 3600)
        seconds %= 3600
        minutes = math.floor(seconds / 60)
        seconds %= 60
        milliseconds = round((seconds - math.floor(seconds)) * 1000)
        seconds = math.floor(seconds)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"
