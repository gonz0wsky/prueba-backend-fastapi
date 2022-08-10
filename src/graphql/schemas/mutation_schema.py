""" Graphql Mutation Schema """
import strawberry

from src.graphql.resolvers.login_resolver import login_user
from src.graphql.types.user_type import UserType
from src.graphql.resolvers.register_resolver import create_user

@strawberry.type
class Mutation:
    """ Mutations """
    login: UserType = strawberry.mutation(resolver=login_user)
    register: UserType = strawberry.mutation(resolver=create_user)
