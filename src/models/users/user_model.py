""" User model """
from tortoise import fields, models
from src.graphql.types.user_type import UserType
class User(models.Model):
    """ User model """
    created_at = fields.DatetimeField(auto_now_add=True)
    email = fields.CharField(unique=True, max_length=255)
    first_name = fields.CharField(max_length=30)
    hash = fields.CharField(max_length=128)
    id = fields.UUIDField(pk=True)
    last_name = fields.CharField(max_length=30)
    modified_at = fields.DatetimeField(auto_now=True)
    username = fields.CharField(max_length=40)
    ideas = fields.ReverseRelation["Idea"]

    def full_name(self) -> str:
        """ Return full name of user """
        return f"{self.first_name or ''} {self.last_name or ''}".strip()

    def to_type(self) -> UserType:
        """ transform class to graphql type"""
        return UserType(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            username=self.full_name(),
            ideas=self.ideas
        )
