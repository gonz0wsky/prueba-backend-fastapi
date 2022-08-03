""" Graphql Mutation Schema """
import strawberry

from src.graphql.types.user_type import User
from src.graphql.resolvers.user_resolver import get_user

@strawberry.type
class Mutation:
    """ Mutations """

    @strawberry.mutation
    async def register(self) -> User:
        """ Register a new user """
        user = await get_user()
        return user
