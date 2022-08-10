""" Config file """
import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    """ Settings """
    class Config:
        """ env config """
        env_file = '.env'
        env_file_encoding = 'utf-8'

    DB_USER: str = os.environ.get("DB_USER")
    DB_PASSWORD: str = os.environ.get("DB_PASSWORD")
    DB_SERVER: str = os.environ.get("DB_SERVER")
    DB_PORT: str = os.environ.get("DB_PORT")
    DB_NAME: str = os.environ.get("DB_NAME")
    HOST_URL: str = os.environ.get("HOST_NAME", "127.0.0.1")
    HOST_PORT: str = os.environ.get("HOST_PORT", "3000")

settings = Settings()
