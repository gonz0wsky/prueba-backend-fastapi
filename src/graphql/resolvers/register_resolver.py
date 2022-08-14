""" Register resolver"""
from src.auth.hash import hash_password
from src.graphql.inputs.register_input import  RegisterInput
from src.graphql.types.user_type import UserType
from src.models.users.user_model import User

async def create_user(data: RegisterInput) -> UserType:
    """ Register an user """
    try:

        hashed_password: str = hash_password(data.password)

        user: User = await User.create(
            email=data.email,
            first_name=data.first_name,
            last_name=data.last_name,
            hash=hashed_password,
        )

        return UserType(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            token="TOKEN"
        )
    except Exception as error:
        raise Exception("Error creating user") from error
