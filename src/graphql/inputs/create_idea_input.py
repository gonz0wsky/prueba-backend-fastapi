""" Create idea Input """
import strawberry
from src.graphql.types.idea_type import IdeaVisibilityType

@strawberry.input
class CreateIdeaInput:
    """ Create idea Input """
    content: str
    visibility: IdeaVisibilityType
