""" Request restore password link """
from src.graphql.inputs.request_restore_password_input import RequestRestorePasswordInput
from src.auth.strategy import create_access_token
from src.models.users.user_model import User

async def request_restore_password_link(data: RequestRestorePasswordInput) -> bool:
    """ Request restore password link """
    try:
        user: User = await User.get(email=data.email)

        restore_token: str = create_access_token(user.id)

        print(f"Send email to: {user.email}")
        print (f"Restore token: {restore_token}")

        return True

    except Exception as error:
        raise Exception("Error requesting restore password link") from error
