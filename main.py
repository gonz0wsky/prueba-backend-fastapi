""" Main file for the application. """
import uvicorn
from src.app import create_app
from src.core.config import settings

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.HOST_URL, port=int(settings.HOST_PORT), reload=True)
