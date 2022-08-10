""" User type. """
import strawberry

@strawberry.type
class UserType:
    """ User type. """
    id: int
    first_name: str
    last_name: str
    token: str
