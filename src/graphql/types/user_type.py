""" User type. """
import strawberry

@strawberry.type
class User:
    """ User type. """
    id: int
    first_name: str
    last_name: str
    token: str
