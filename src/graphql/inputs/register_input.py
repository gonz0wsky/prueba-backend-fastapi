""" Register Input """
from typing import Optional
import strawberry

@strawberry.input
class RegisterInput:
    """ Register Input """
    email: str
    first_name: str
    last_name: Optional[str]
    password: str
    username: str
