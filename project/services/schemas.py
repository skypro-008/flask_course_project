from marshmallow import Schema
from marshmallow.fields import Email, Str


class UserSchema(Schema):
    email = Email(required=True)
    password = Str(required=True, load_only=True)
    name = Str()
    surname = Str()

