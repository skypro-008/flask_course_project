from flask_restx import Namespace, Resource

from project.services.main import DirectorsService, GenresService, MoviesService
from project.setup import db
from project.setup.api.models import director, error, genre, movie
from project.setup.api.parsers import movie_state_parser, pages_parser

genres_ns = Namespace('genres')


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


directors_ns = Namespace('directors')


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


movies_ns = Namespace('movies')


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
