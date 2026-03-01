import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    # --- Database ---
    DATABASE_URL: str = "postgresql://n8n:n8npassword@postgres:5432/n8n"

    # --- AI Providers ---
    OLLAMA_URL: str = "http://ollama:11434"
    OLLAMA_MODEL: str = "llama3:latest"
    
    GEMINI_API_KEY: Optional[str] = None
    NOTION_TOKEN: Optional[str] = "ntn_490158019409893d0490"
    NOTION_DB_ID: Optional[str] = "3128c751-d8ee-81a8-a331-fca0292426a0"
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
    
    # --- New Integrations v12.5 ---
    GROQ_API_KEY: Optional[str] = None
    REMOVE_BG_API_KEY: Optional[str] = None
    GOOGLE_SHEETS_ID: Optional[str] = None

    # --- Communication ---
    TELEGRAM_TOKEN: Optional[str] = None
    TELEGRAM_CHAT_ID: Optional[str] = None

    # --- Directories ---
    DATA_MIDIA: str = "C:/Users/Usuario/Desktop/meu-freshrss/data_midia" if os.name == "nt" else "/data_midia"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
