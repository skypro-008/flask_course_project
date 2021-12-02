from http import HTTPStatus

from flask_restx import fields, Namespace, Resource

from project.services.items import DirectorsService, GenresService, MoviesService
from project.tools.setup_db import db
from project.views.dto import movie_state_parser, pages_parser

directors_ns = Namespace('directors', validate=True)
genres_ns = Namespace('genres', validate=True)
movies_ns = Namespace('movies', validate=True)

director = directors_ns.model('Режиссер', {
    'id': fields.Integer(required=True),
    'name': fields.String
})

genre = genres_ns.clone('Жанр', director)


@directors_ns.route('/')
class DirectorsView(Resource):

    @directors_ns.expect(pages_parser)
    @directors_ns.response(int(HTTPStatus.OK), 'OK')
    @directors_ns.marshal_list_with(director)
    def get(self):
        """ Get all directors """
        return DirectorsService(db.session).get_all(**pages_parser.parse_args()), HTTPStatus.OK


@directors_ns.route('/<int:director_id>')
class DirectorView(Resource):

    @directors_ns.response(int(HTTPStatus.OK), 'OK', director)
    @directors_ns.response(int(HTTPStatus.NOT_FOUND), 'Director not found')
    @directors_ns.marshal_with(director)
    def get(self, director_id: int):
        """ Get movie by id """
        return DirectorsService(db.session).get_item(director_id), HTTPStatus.OK


@genres_ns.route('/')
class GenresView(Resource):

    @genres_ns.expect(pages_parser)
    @genres_ns.response(int(HTTPStatus.OK), 'OK')
    @genres_ns.marshal_list_with(genre)
    def get(self):
        """ Get all genres """
        return GenresService(db.session).get_all(**pages_parser.parse_args()), HTTPStatus.OK


@genres_ns.route('/<int:genre_id>')
class GenreView(Resource):

    @genres_ns.response(int(HTTPStatus.OK), 'OK', genre)
    @genres_ns.response(int(HTTPStatus.NOT_FOUND), 'Genre not found')
    @genres_ns.marshal_with(genre)
    def get(self, genre_id: int):
        """ Get genre by id """
        return GenresService(db.session).get_item(genre_id), HTTPStatus.OK


@movies_ns.route('/')
class MoviesView(Resource):

    @movies_ns.expect(movie_state_parser)
    @movies_ns.response(int(HTTPStatus.OK), 'OK')
    def get(self):
        """ Get all movies """
        return MoviesService(db.session).get_all(**movie_state_parser.parse_args()), HTTPStatus.OK


@movies_ns.route('/<int:movie_id>')
class MovieView(Resource):

    @movies_ns.response(int(HTTPStatus.OK), 'OK')
    @movies_ns.response(int(HTTPStatus.NOT_FOUND), 'Movie not found')
    def get(self, movie_id: int):
        """ Get movie by id """
        return MoviesService(db.session).get_item(movie_id), HTTPStatus.OK
