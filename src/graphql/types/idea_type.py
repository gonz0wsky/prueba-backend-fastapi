""" Idea type. """
from enum import Enum
from typing import TYPE_CHECKING, Annotated
import strawberry
from src.models.idea.idea_model import IdeaVisibility

if TYPE_CHECKING:
    from .user_type import UserType

@strawberry.enum
class IdeaVisibilityType(Enum):
    """ Idea visibility type """
    PRIVATE = IdeaVisibility.PRIVATE
    PROTECTED = IdeaVisibility.PROTECTED
    PUBLIC = IdeaVisibility.PUBLIC

@strawberry.type
class IdeaType:
    """ Idea type """
    author: Annotated["UserType", strawberry.lazy(".user_type")]
    content: str
    id: str
    visibility: IdeaVisibilityType
