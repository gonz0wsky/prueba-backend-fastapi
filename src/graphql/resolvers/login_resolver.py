""" Login resolver"""
from src.auth.hash import check_password
from src.models.users.user_model import User
from src.graphql.types.user_type import UserType
from src.graphql.inputs.login_input import LoginInput

async def login_user(data: LoginInput) -> UserType:
    """ Login """
    try:

        user: User = await User.get(email=data.email)

        is_valid_password: bool = check_password(data.password, user.hash)

        if not is_valid_password:
            raise Exception("Invalid credentials")

        return UserType(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            token="TOKEN"
        )
    except Exception as error:
        raise Exception("Invalid credentials") from error
