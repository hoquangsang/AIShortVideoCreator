from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ### PORT
    PORT: int = 8000

    class Config:
        extra = "allow"
        env_file = ".env"
        env_file_encoding = "utf-8"

app_settings = Settings()