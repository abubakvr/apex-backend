import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "My FastAPI App"
    APP_VERSION = "1.0.0"
    MONGODB_URI = os.getenv("MONGODB_URI")
    BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
    BYBIT_SECRET_KEY= os.getenv("BYBIT_SECRET_KEY")
    if MONGODB_URI is None:
        raise ValueError("MONGODB_URI environment variable not set.")
    HOST = "0.0.0.0"  # Or "127.0.0.1" for localhost
    PORT = 8001

settings = Settings()