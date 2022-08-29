""" User type. """
from typing import Optional
import strawberry


@strawberry.type
class UserType:
    """ User type. """
    first_name: str
    id: str
    last_name: Optional[str]
    username: str
