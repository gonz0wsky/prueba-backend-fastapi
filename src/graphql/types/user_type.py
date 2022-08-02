import strawberry

@strawberry.type
class UserType:
    id: int
    first_name: str
    last_name: str
    token: str
