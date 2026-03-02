import os
from dotenv import load_dotenv


load_dotenv()

#  gets the key as well as model name and prompt from .env file where the sensitive data is stored
class Settings:
    GROQ_API_KEY  = os.getenv("GROQ_API_KEY")
    MODEL_NAME    = os.getenv("MODEL_NAME")
    SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT")

settings = Settings()