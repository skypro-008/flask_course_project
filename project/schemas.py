from datetime import datetime

from marshmallow import pre_load, Schema
from marshmallow.fields import Email, Float, Int, Nested, Str
from marshmallow.validate import Range


class BaseSchema(Schema):
    id = Int(dump_only=True)

    @pre_load
    def skip_empty_values(self, data, **kwargs):
        return {k: v for k, v in data.items() if v}


class GenreSchema(BaseSchema):
    name = Str(required=True)


class DirectorSchema(BaseSchema):
    name = Str(required=True)


class MovieSchema(BaseSchema):
    title = Str(required=True)
    description = Str(required=True)
    year = Int(required=True, validate=Range(min=0, max=datetime.now().year))
    rating = Float(validate=Range(min=0, max=10))
    genre_id = Int(load_only=True, required=True)
    director_id = Int(load_only=True, required=True)
    genre = Nested(GenreSchema, dump_only=True)
    director = Nested(DirectorSchema, dump_only=True)


class UserSchema(BaseSchema):
    email = Email(required=True)
    password = Str(required=True, load_only=True)
    name = Str()
    surname = Str()
    favourite_genre = Int()
    favorites = Nested(MovieSchema(only=('id',)), dump_only=True)
