from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    # --- Database ---
    DATABASE_URL: str = "postgresql://n8n:n8npassword@postgres:5432/n8n"

    # --- AI Providers ---
    OLLAMA_URL: str = "http://ollama:11434"
    OLLAMA_MODEL: str = "llama3"
    
    GEMINI_API_KEY: Optional[str] = None
    CLAUDE_API_KEY: Optional[str] = None
    OPENAI_API_KEY: Optional[str] = None
    DEEPAI_API_KEY: Optional[str] = None
    STABILITY_API_KEY: Optional[str] = None
    
    # --- Stock Images ---
    PEXELS_API_KEY: Optional[str] = None
    PIXABAY_API_KEY: Optional[str] = None
    UNSPLASH_ACCESS_KEY: Optional[str] = None
    
    # --- TTS Keys ---
    GOOGLE_APPLICATION_CREDENTIALS: Optional[str] = None
    AZURE_SPEECH_KEY: Optional[str] = None
    AZURE_SPEECH_REGION: Optional[str] = None
    UNREAL_SPEECH_API_KEY: Optional[str] = None
    
    # --- Search / Trends ---
    TAVILY_API_KEY: Optional[str] = None
    SERPER_API_KEY: Optional[str] = None
    BRAVE_API_KEY: Optional[str] = None
    GOOGLE_CUSTOM_SEARCH_KEY: Optional[str] = None
    GOOGLE_CUSTOM_SEARCH_CX: Optional[str] = None

    # --- Directories ---
    DATA_MIDIA: str = "/data_midia"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
