""" Login resolver"""
from strawberry.types import Info
from src.auth.hash import check_password, hash_password
from src.models.users.user_model import User
from src.graphql.inputs.change_password_input import ChangePasswordInput

async def change_user_password(data: ChangePasswordInput, info: Info) -> bool:
    """ Change password """
    try:
        user_id: str = info.context['user']
        user: User = await User.get(id=user_id)
        is_valid_password: bool = check_password(data.current_password, user.hash)

        if not is_valid_password:
            raise Exception("Error changing password")

        user.hash = hash_password(data.new_password)
        await User.save(user)

        return True

    except Exception as error:
        raise Exception("Error changing password") from error
