""" App file for the application. """
from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig

from src.graphql.schemas.query_schema import Query
from src.graphql.schemas.mutation_schema import Mutation

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    config=StrawberryConfig(auto_camel_case=True))

def create_app():
    """ Create app function. """
    app = FastAPI()

    graphql_app = GraphQLRouter(schema)
    app.include_router(graphql_app, prefix="/graphql")

    return app
