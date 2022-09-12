""" Create idea resolver"""
from strawberry.types import Info
from tortoise.exceptions import DoesNotExist
from src.models.users.user_model import User
from src.graphql.inputs.create_idea_input import CreateIdeaInput
from src.graphql.types.idea_type import IdeaType
from src.models.idea.idea_model import Idea

async def create_idea(data: CreateIdeaInput, info: Info) -> IdeaType:
    """ Create idea """
    try:
        user_id: str = info.context['user']
        user: User = await User.get(id=user_id)

        idea: Idea = await Idea.create(
            author=user,
            content=data.content,
            visibility=data.visibility.value
        )

        return IdeaType(
            author=user.to_type(),
            content=idea.content,
            id=idea.id,
            visibility=idea.visibility,
        )

    except DoesNotExist as exc:
        raise DoesNotExist("Invalid credentials") from exc
    except Exception as error:
        raise Exception("Error creating an idea") from error
