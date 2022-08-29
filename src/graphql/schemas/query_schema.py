""" Graphql Query Schema """
import strawberry
from src.auth.auth_guard import AuthGuard
from src.graphql.resolvers.user_resolver import get_user

@strawberry.type
class Query:
    """ Queries """
    user = strawberry.field(permission_classes=[AuthGuard], resolver=get_user)
