from pydantic import ConfigDict
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ### PORT
    PORT: int = 8000

    ### Mongo Uri
    MONGODB_URI: str
    MONGODB_NAME: str

    model_config = ConfigDict(
        extra="allow",
        env_file=".env",
        env_file_encoding="utf-8",
    )

app_settings = Settings()