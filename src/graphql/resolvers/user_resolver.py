from src.graphql.types.user_type import UserType

async def get_user():
    """Get logged user resolver"""
    user = UserType(id=1, first_name="John", last_name="Doe", token="abc")
    return user