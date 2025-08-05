from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # APP INFO & ENV
    APP_NAME: str = 'AI Short Video Creator'
    APP_VERSION: str = '1.0.0'
    APP_ENV: str = 'development'
    LOG_LEVEL: str = 'debug'
    LOG_DIR: str = 'logs'

    # SERVER CONFIG
    HOST: str = '0.0.0.0'
    PORT: int = 8000
    BASE_URL: str = 'http://localhost:8000'


    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='allow',
    )


    @property
    def IS_DEV_MODE(self) -> bool:
        return self.APP_ENV == 'development'

settings = Settings()