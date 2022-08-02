import strawberry

from src.graphql.types.user_type import UserType
from src.graphql.resolvers.user_resolver import get_user

@strawberry.type
class Query:

    @strawberry.field
    async def me(self) -> UserType:
        """ Get me user """
        user = await get_user()
        return user
