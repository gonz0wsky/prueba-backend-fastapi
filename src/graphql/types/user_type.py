""" User type. """
from typing import Optional, TYPE_CHECKING, Annotated, List
import strawberry

if TYPE_CHECKING:
    from .idea_type import IdeaType
@strawberry.type
class UserType:
    """ User type """
    first_name: str
    id: str
    last_name: Optional[str]
    username: str
    ideas: List[Annotated["IdeaType", strawberry.lazy(".idea_type")]]
