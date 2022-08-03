""" User resolver"""
from src.graphql.types.user_type import User

async def get_user():
    """Get logged user resolver"""
    user = User(id=1, first_name="John", last_name="Doe", token="abc")
    return user
