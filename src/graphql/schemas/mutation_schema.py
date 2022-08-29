""" Graphql Mutation Schema """
import strawberry
from src.auth.auth_guard import AuthGuard
from src.graphql.resolvers.change_password_resolver import change_user_password
from src.graphql.resolvers.login_resolver import login_user
from src.graphql.resolvers.register_resolver import create_user

@strawberry.type
class Mutation:
    """ Mutations """
    login = strawberry.mutation(resolver=login_user)
    register = strawberry.mutation(resolver=create_user)
    change_password = strawberry.mutation(permission_classes=[AuthGuard], resolver=change_user_password)
