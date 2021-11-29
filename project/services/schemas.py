from marshmallow import Schema
from marshmallow.fields import Email, Str
from marshmallow_enum import EnumField

from project.tools.enums import UserRole


class UserSchema(Schema):
    email = Email(required=True)
    password_hash = Str(required=True, load_only=True, data_key="password")
    name = Str()
    surname = Str()
    role = EnumField(UserRole, load_by=EnumField.VALUE, required=True)
