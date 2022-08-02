import strawberry

from src.graphql.inputs.register_input import RegisterInput
from src.graphql.types.user_type import UserType
from src.graphql.resolvers.user_resolver import get_user

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def register(self, input: RegisterInput) -> UserType:
        """ Register a new user """
        user = await get_user()
        return user
