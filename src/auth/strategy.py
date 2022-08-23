""" JWT token """
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt
from fastapi import Depends, HTTPException, status

from src.models.users.user_model import User
from src.core.config import settings

def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    """ Create a new access token """
    expire_minutes: float = float(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    jwt_secret_key: str = settings.JWT_SECRET_KEY
    algorithm: str = settings.ALGORITHM

    print(expire_minutes, jwt_secret_key, algorithm)

    delta = expires_delta or timedelta(minutes=expire_minutes)
    exp = datetime.utcnow() + delta

    to_encode = {"exp": exp, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, jwt_secret_key, algorithm)
    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    """ Creates a refresh token """
    expire_minutes: float = float(settings.REFRESH_TOKEN_EXPIRE_MINUTES)
    jwt_secret_key: str = settings.JWT_SECRET_KEY
    algorithm: str = settings.ALGORITHM

    delta = expires_delta or timedelta(minutes=expire_minutes)
    exp = datetime.utcnow() + delta

    to_encode = {"exp": exp, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, jwt_secret_key, algorithm)
    return encoded_jwt

async def authenticate_user(token: str) -> User:
    """ Get the current user"""
    try:
        jwt_secret_key: str = settings.JWT_SECRET_KEY
        algorithm: str = settings.ALGORITHM

        payload = jwt.decode(token, jwt_secret_key, algorithms=[algorithm])

        timestamp = payload.get('exp')
        if datetime.fromtimestamp(timestamp) < datetime.now():
            raise Exception("Token expired")

        user_id = payload.get('sub')
        user: User = await User.get(id=user_id)

        return user

    except Exception as error:
        raise Exception("Invalid token") from error
