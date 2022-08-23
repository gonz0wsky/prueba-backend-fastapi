""" Auth guard """
import typing
from strawberry.permission import BasePermission
from strawberry.types import Info
from starlette.requests import Request
from starlette.websockets import WebSocket
from src.models.users.user_model import User

from src.auth.strategy import authenticate_user

class AuthGuard(BasePermission):
    """ Check if user is authenticated """

    message = "User is not authenticated"

    async def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        # pylint: disable=invalid-overridden-method

        request: typing.Union[Request, WebSocket] = info.context["request"]

        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
            user: User = await authenticate_user(token)

            if user is None:
                return False

            return True

        return False
