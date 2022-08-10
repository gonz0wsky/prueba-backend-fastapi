""" Graphql Query Schema """
import strawberry

from src.graphql.types.user_type import UserType
from src.graphql.resolvers.user_resolver import get_user

@strawberry.type
class Query:
    """ Queries """

    @strawberry.field
    async def user(self) -> UserType:
        """ Get me user """
        user = await get_user()
        return user
