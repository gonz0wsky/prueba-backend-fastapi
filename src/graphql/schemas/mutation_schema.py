""" Graphql Mutation Schema """
import strawberry

from src.graphql.types.user_type import UserType
from src.graphql.resolvers.user_resolver import get_user

@strawberry.type
class Mutation:
    """ Mutations """

    @strawberry.mutation
    async def register(self) -> UserType:
        """ Register a new user """
        user = await get_user()
        return user
