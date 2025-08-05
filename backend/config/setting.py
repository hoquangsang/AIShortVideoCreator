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

    # CORS (raw)
    CORS_ALLOW_ORIGINS: str = '*'
    CORS_ALLOW_METHODS: str = '*'
    CORS_ALLOW_HEADERS: str = '*'
    CORS_ALLOW_CREDENTIALS: bool = True

    # Database
    MONGODB_URI: str
    MONGODB_DATABASE: str

    # TODO

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='allow',
    )

    @property
    def CORS_ALLOW_ORIGINS_LIST(self) -> list[str]:
        return [i.strip() for i in self.CORS_ALLOW_ORIGINS.split(',')]
    @property
    def CORS_ALLOW_METHODS_LIST(self) -> list[str]:
        return [i.strip() for i in self.CORS_ALLOW_METHODS.split(',')]
    @property
    def CORS_ALLOW_HEADERS_LIST(self) -> list[str]:
        return [i.strip() for i in self.CORS_ALLOW_HEADERS.split(',')]

    @property
    def IS_DEV_MODE(self) -> bool:
        return self.APP_ENV == 'development'

settings = Settings()