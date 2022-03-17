from flask_restx import fields, Namespace, Resource

from project.services.items import DirectorsService, GenresService, MoviesService
from project.setup_db import db
from project.views.dto import movie_state_parser, pages_parser
from project.views.err import error

genres_ns = Namespace('genres', validate=True)
genre = genres_ns.model('Жанр', {
    'id': fields.Integer,
    'name': fields.String,
})


@genres_ns.route('/')
class GenresView(Resource):
    @genres_ns.expect(pages_parser)
    @genres_ns.marshal_with(genre, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all genres.
        """
        return GenresService(db.session).get_all(**pages_parser.parse_args())


@genres_ns.route('/<int:genre_id>')
class GenreView(Resource):
    @genres_ns.response(404, 'Not Found', error)
    @genres_ns.marshal_with(genre, code=200, description='OK')
    def get(self, genre_id: int):
        """
        Get genre by id.
        """
        return GenresService(db.session).get_item(genre_id)


directors_ns = Namespace('directors', validate=True)
director = directors_ns.model('Режиссер', {
    'id': fields.Integer,
    'name': fields.String,
})


@directors_ns.route('/')
class DirectorsView(Resource):
    @directors_ns.expect(pages_parser)
    @directors_ns.marshal_with(director, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all directors.
        """
        return DirectorsService(db.session).get_all(**pages_parser.parse_args())


@directors_ns.route('/<int:director_id>')
class DirectorView(Resource):
    @directors_ns.response(404, 'Not Found', error)
    @directors_ns.marshal_with(director, code=200, description='OK')
    def get(self, director_id: int):
        """
        Get director by id
        """
        return DirectorsService(db.session).get_item(director_id)


movies_ns = Namespace('movies', validate=True)
movie = directors_ns.model('Фильм', {
    'id': fields.Integer,
    'name': fields.String,
})


@movies_ns.route('/')
class MoviesView(Resource):
    @movies_ns.expect(movie_state_parser)
    @movies_ns.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all movies.
        """
        return MoviesService(db.session).get_all(**movie_state_parser.parse_args())


@movies_ns.route('/<int:movie_id>')
class MovieView(Resource):
    @directors_ns.response(404, 'Not Found', error)
    @directors_ns.marshal_with(movie, code=200, description='OK')
    def get(self, movie_id: int):
        """
        Get movie by id.
        """
        return MoviesService(db.session).get_item(movie_id)
