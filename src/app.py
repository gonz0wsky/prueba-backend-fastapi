""" App file for the application. """
from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig
from src.graphql.middlewares.token_middleware import TokenMiddleware
from src.db.db import init_db
from src.graphql.schemas.query_schema import Query
from src.graphql.schemas.mutation_schema import Mutation

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    config=StrawberryConfig(auto_camel_case=True),
    extensions=[
        TokenMiddleware
    ])

def create_app():
    """ Create app function. """
    app = FastAPI()

    init_db(app)

    graphql_app = GraphQLRouter(schema)
    app.include_router(graphql_app, prefix="/graphql")

    return app
