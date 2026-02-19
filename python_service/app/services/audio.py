
import os
import re
import edge_tts
from app.config import settings

class AudioService:
    def __init__(self):
        # Voz masculina brasileira, boa para notícias
        self.voice = "pt-BR-AntonioNeural" 
        self.output_dir = os.path.join(settings.DATA_MIDIA, "audios")
        os.makedirs(self.output_dir, exist_ok=True)

    def clean_text(self, text: str) -> str:
        """Remove markdown, URLs e caracteres especiais que atrapalham o TTS."""
        if not text: return ""
        # Remove URLs
        text = re.sub(r'http\S+', '', text)
        # Remove Markdown bold/italic
        text = text.replace('*', '').replace('_', '')
        # Remove emojis (tenta manter texto limpo)
        # text = text.encode('ascii', 'ignore').decode('ascii') # removido pois remove acentos portugueses
        # Remove espaços extras
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    async def generate(self, text: str, job_id: str) -> str:
        """Gera áudio MP3 a partir do texto usando Edge TTS."""
        clean_text = self.clean_text(text)
        if not clean_text:
            print(f"[AudioService] Texto vazio para job {job_id}")
            return ""
            
        output_path = os.path.join(self.output_dir, f"{job_id}.mp3")
        
        try:
            communicate = edge_tts.Communicate(clean_text, self.voice)
            await communicate.save(output_path)
            
            if os.path.exists(output_path):
                 print(f"[AudioService] Áudio gerado com sucesso: {output_path}")
                 return output_path
            else:
                 raise RuntimeError("Arquivo de áudio não encontrado após geração.")
        except Exception as e:
            print(f"[AudioService] Erro ao gerar áudio: {e}")
            raise e
