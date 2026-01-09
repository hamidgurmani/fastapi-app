from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Sample App"
    ENVIRONMENT: str = "development"
    PORT: int = 8000

    class Config:
        env_file = ".env"

settings = Settings()

