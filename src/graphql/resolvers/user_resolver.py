""" User resolver"""
from strawberry.types import Info
from src.models.users.user_model import User
from src.models.idea.idea_model import Idea
from src.graphql.types.user_type import UserType

async def get_user(info: Info) -> UserType:
    """Get logged user resolver"""
    try:
        user_id: str = info.context['user']
        user: User = await User.get(id=user_id)
        ideas: list[Idea] = await Idea.filter(author=user)

        return UserType(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username,
            ideas=ideas)

    except Exception as error:
        raise Exception("Error getting user") from error
