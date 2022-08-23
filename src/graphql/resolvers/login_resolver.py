""" Login resolver"""
from src.auth.strategy import create_access_token
from src.auth.hash import check_password
from src.models.users.user_model import User
from src.graphql.inputs.login_input import LoginInput

async def login_user(data: LoginInput) -> str:
    """ Login """
    try:
        user: User = await User.get(email=data.email)

        if user is None:
            raise Exception("Invalid credentials")

        is_valid_password: bool = check_password(data.password, user.hash)

        if not is_valid_password:
            raise Exception("Invalid credentials")

        return create_access_token(user.id)

    except Exception as error:
        raise Exception("Invalid credentials") from error
