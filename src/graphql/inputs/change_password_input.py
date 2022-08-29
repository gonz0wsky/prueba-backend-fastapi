""" Change password input """
import strawberry

@strawberry.input
class ChangePasswordInput:
    """ Change password input """
    current_password: str
    new_password: str
