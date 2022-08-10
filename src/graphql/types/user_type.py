""" User type. """
from typing import Optional
import strawberry


@strawberry.type
class UserType:
    """ User type. """
    id: str
    first_name: str
    last_name: Optional[str]
    token: str
