""" Graphql Mutation Schema """
from venv import create
import strawberry

from src.graphql.types.user_type import UserType
from src.graphql.resolvers.register_resolver import create_user

@strawberry.type
class Mutation:
    """ Mutations """
    register: UserType = strawberry.mutation(resolver=create_user)
