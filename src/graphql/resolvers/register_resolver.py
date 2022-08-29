""" Register resolver"""
from src.auth.strategy import create_access_token
from src.auth.hash import hash_password
from src.graphql.inputs.register_input import  RegisterInput
from src.models.users.user_model import User

async def create_user(data: RegisterInput) -> str:
    """ Register an user """
    try:
        hashed_password: str = hash_password(data.password)

        user: User = await User.create(
            email=data.email,
            first_name=data.first_name,
            hash=hashed_password,
            last_name=data.last_name,
            username=data.username
        )

        token = create_access_token(user.id)
        return token

    except Exception as error:
        raise Exception("Error creating user") from error
