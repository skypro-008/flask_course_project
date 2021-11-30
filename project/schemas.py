from datetime import datetime
from typing import Type

from flask_sqlalchemy.model import Model
from marshmallow import post_load, Schema
from marshmallow.fields import Email, Float, Int, Nested, Str
from marshmallow.validate import Range

from project.models import Director, Genre, Movie, User


class BaseSchema(Schema):
    __model__: Type[Model] = NotImplemented

    id = Int(dump_only=True)

    @post_load
    def make_object(self, data, **kwargs):
        return self.__model__(**data)


class GenreSchema(BaseSchema):
    __model__ = Genre

    name = Str(required=True)


class DirectorSchema(BaseSchema):
    __model__ = Director

    name = Str(required=True)


class MovieSchema(BaseSchema):
    __movie__ = Movie

    title = Str(required=True)
    description = Str(required=True)
    year = Int(required=True, validate=Range(min=0, max=datetime.now().year))
    rating = Float(validate=Range(min=0, max=10))
    genre_id = Int(load_only=True, required=True)
    director_id = Int(load_only=True, required=True)
    genre = Nested(GenreSchema, dump_only=True)
    director = Nested(DirectorSchema, dump_only=True)


class UserSchema(BaseSchema):
    __model__ = User

    email = Email(required=True)
    password = Str(required=True, load_only=True)
    name = Str()
    surname = Str()
    favourite_genre = Nested(GenreSchema, dump_only=True)
    favorites = Nested(MovieSchema(only=('id',)), dump_only=True)
