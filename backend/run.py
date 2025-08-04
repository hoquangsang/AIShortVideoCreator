import uvicorn
from app import create_app
from config.setting import settings 

app = create_app()

def main():
    uvicorn.run(
        "run:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.APP_ENV.lower() == 'development',
        log_level=settings.LOG_LEVEL,
    )

if __name__ == "__main__":
    main()