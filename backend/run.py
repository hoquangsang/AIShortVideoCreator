import uvicorn
from app import create_app
from config import app_settings 

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "run:app",
        host="0.0.0.0",
        port=app_settings.PORT,
        reload=True,
        log_level="debug",
    )