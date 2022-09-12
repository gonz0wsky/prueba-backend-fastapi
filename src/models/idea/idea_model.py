""" Idea model """
from tortoise import fields, models
from src.models.idea.idea_visibility import IdeaVisibility
from src.models.users.user_model import User
from src.graphql.types.idea_type import IdeaType

class Idea(models.Model):
    """ Idea model """
    id = fields.UUIDField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    content = fields.TextField()
    author: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User", related_name="ideas", to_field="id"
    )
    visibility = fields.CharEnumField(IdeaVisibility, default=IdeaVisibility.PUBLIC)

    def to_type(self) -> IdeaType:
        """ transform class to graphql type"""
        return IdeaType(
            id=self.id,
            author=self.author,
            content=self.content,
            visibility=self.visibility,
        )
