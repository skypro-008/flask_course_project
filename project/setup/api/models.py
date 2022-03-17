from flask_restx import fields, Model

from project.setup.api import api

# TODO: Добавить примеров https://flask-restx.readthedocs.io/en/latest/swagger.html
error: Model = api.model('Сообщение об ошибке', {
    'message': fields.String(required=True, example='Error description'),
})

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=2),
    'name': fields.String(required=True, max_length=100, example='Квентин Тарантино'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=255, example='Йеллоустоун'),
    'description': fields.String(
        required=True,
        example="Владелец ранчо пытается сохранить землю своих предков. "
                "Кевин Костнер в неовестерне от автора «Ветреной реки"
    ),
    'trailer': fields.String(max_length=255, example="https://www.youtube.com/watch?v=UKei_d0cbP4"),
    'year': fields.Integer(required=True, min=0, example=2018),
    'rating': fields.Float(required=True, min=0.0, max=10.0, example=8.6),
    'genre': fields.Nested(genre, required=True),
    'director': fields.Nested(director, required=True),
})
