""" db """
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.core.config import settings

db_url: str = f"postgres://" \
    f"{settings.DB_USER}:{settings.DB_PASSWORD}@" \
    f"{settings.DB_SERVER}:{settings.DB_PORT}/" \
    f"{settings.DB_NAME}"

TORTOISE_ORM = {
    "connections": {"default": db_url},
    "apps": {
        "models": {
            "models": ["src.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

def init_db(app: FastAPI) -> None:
    """ Initialize database. """

    register_tortoise(
    app,
    db_url=db_url,
    modules={"models": ["src.models"]},
    generate_schemas=True,
    add_exception_handlers=True)
