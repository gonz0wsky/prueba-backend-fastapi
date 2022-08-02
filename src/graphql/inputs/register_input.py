import strawberry
from pydantic import typing

@strawberry.input
class RegisterInput:
    email: str
    first_name: str
    last_name: typing.Optional[str]
    password: str
