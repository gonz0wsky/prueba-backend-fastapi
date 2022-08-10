""" Graphql Query Schema """
import strawberry

from src.graphql.types.user_type import UserType
from src.graphql.resolvers.user_resolver import get_user

@strawberry.type
class Query:
    """ Queries """
    user: UserType = strawberry.field(resolver=get_user)
