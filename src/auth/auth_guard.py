""" Auth guard """
import typing
from strawberry.permission import BasePermission
from strawberry.types import Info
from starlette.requests import Request
from starlette.websockets import WebSocket

class AuthGuard(BasePermission):
    """ Check if user is authenticated """

    message = "User is not authenticated"

    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        request: typing.Union[Request, WebSocket] = info.context["request"]

        if "Authorization" in request.headers:
            # TODO: Check if token is valid
            return True

        return False
