from marshmallow.fields import Email, Int, Str
from marshmallow.validate import OneOf

from project.services.schemas import BaseSchema


class CredentialsValidator(BaseSchema):
    email = Email(required=True)
    password = Str(required=True, load_only=True)


class TokenValidator(BaseSchema):
    access_token = Str(required=True)
    refresh_token = Str(required=True)


class PageValidator(BaseSchema):
    page = Int(required=False)


class MovieStateValidator(PageValidator):
    state = Str(validate=OneOf(["new"]), required=False)
