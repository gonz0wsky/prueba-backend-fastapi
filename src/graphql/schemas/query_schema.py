""" Graphql Query Schema """
import strawberry

from src.graphql.types.user_type import User
from src.graphql.resolvers.user_resolver import get_user

@strawberry.type
class Query:
    """ Queries """

    @strawberry.field
    async def user(self) -> User:
        """ Get me user """
        user = await get_user()
        return user
