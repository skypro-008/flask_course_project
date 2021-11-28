from marshmallow import post_load, Schema
from marshmallow.fields import Email, Method, Str
from marshmallow_enum import EnumField

from project.enums import UserRole
from project.models import User
from project.tools.security import generate_password_hash


class UserSchema(Schema):
    __model__ = User

    email = Email(required=True)
    password_hash = Method(deserialize='load_password', required=True, load_only=True, data_key="password")
    name = Str()
    surname = Str()
    role = EnumField(UserRole, load_by=EnumField.VALUE, required=True)

    def load_password(self, value):
        return generate_password_hash(value)

    @post_load
    def make_object(self, data, **kwargs):
        return self.__model__(**data)
