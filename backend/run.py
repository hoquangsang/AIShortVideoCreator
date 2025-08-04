import uvicorn
from app import create_app
from config.setting import settings 

app = create_app()

def main():
    uvicorn.run(
        "run:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.IS_DEV_MODE,
        log_level=settings.LOG_LEVEL,
    )

if __name__ == "__main__":
    main()