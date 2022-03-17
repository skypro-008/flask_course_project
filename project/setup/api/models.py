from flask_restx import fields

from project.setup import api

genre = api.model('Жанр', {
    'id': fields.Integer,
    'name': fields.String,
})

director = api.model('Режиссер', {
    'id': fields.Integer,
    'name': fields.String,
})

movie = api.model('Фильм', {
    'id': fields.Integer,
    'name': fields.String,
})
error = api.model('Сообщение об ошибке', {'message': fields.String, })
