""" Restore password """
from tortoise.exceptions import DoesNotExist
from src.auth.hash import hash_password
from src.graphql.inputs.restore_password_input import RestorePasswordInput
from src.auth.strategy import decode_user_id_from_token
from src.models.users.user_model import User

async def restore_password(data: RestorePasswordInput) -> bool:
    """ Restore password """
    try:
        user_id: str = decode_user_id_from_token(data.token)
        user: User = await User.get(id=user_id)

        if not data.password == data.repeat_password:
            raise Exception("Password does not match")

        hashed_password: str = hash_password(data.password)

        user.hash = hashed_password
        await User.save(user)

        return True

    except DoesNotExist as exc:
        raise DoesNotExist("Invalid credentials") from exc
    except Exception as error:
        raise error
