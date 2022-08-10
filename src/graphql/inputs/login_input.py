""" Login Input """
import strawberry

@strawberry.input
class LoginInput:
    """ Login Input """
    email: str
    password: str
