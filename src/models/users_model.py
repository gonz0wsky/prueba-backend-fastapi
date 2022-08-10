""" User model """
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class Users(models.Model):
    """ User model """
    created_at = fields.DatetimeField(auto_now_add=True)
    email = fields.CharField(unique=True, max_length=255)
    first_name = fields.CharField(max_length=30)
    hash = fields.CharField(max_length=128)
    id = fields.UUIDField(pk=True)
    last_name = fields.CharField(max_length=30)
    modified_at = fields.DatetimeField(auto_now=True)

    def full_name(self) -> str:
        """ Return full name of user """
        return f"{self.first_name or ''} {self.last_name or ''}".strip()

    class PydanticMeta:
        """ Pydantic meta class """
        computed = ['full_name']
        excluded = ['hash']

User_Pydantic = pydantic_model_creator(Users, name="User")
UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)
