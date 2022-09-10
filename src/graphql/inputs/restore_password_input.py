""" Restore password input """
import strawberry

@strawberry.input
class RestorePasswordInput:
    """ Restore password input """
    token: str
    password: str
    repeat_password: str
