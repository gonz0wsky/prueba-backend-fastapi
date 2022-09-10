""" Request restore password input """
import strawberry

@strawberry.input
class RequestRestorePasswordInput:
    """ Request restore password input """
    email: str
