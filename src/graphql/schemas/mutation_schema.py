#pylint: disable=line-too-long

""" Graphql Mutation Schema """
import strawberry
from src.auth.auth_guard import AuthGuard
from src.graphql.resolvers.change_password_resolver import change_user_password
from src.graphql.resolvers.create_idea_resolver import create_idea
from src.graphql.resolvers.login_resolver import login_user
from src.graphql.resolvers.register_resolver import create_user
from src.graphql.resolvers.request_restore_password_link_resolver import request_restore_password_link
from src.graphql.resolvers.restore_password_resolver import restore_password

@strawberry.type
class Mutation:
    """ Mutations """
    change_password = strawberry.mutation(permission_classes=[AuthGuard], resolver=change_user_password)
    create_idea = strawberry.mutation(permission_classes=[AuthGuard], resolver=create_idea)
    login = strawberry.mutation(resolver=login_user)
    register = strawberry.mutation(resolver=create_user)
    request_restore_password_link = strawberry.mutation(resolver=request_restore_password_link)
    restore_password = strawberry.mutation(resolver=restore_password)
