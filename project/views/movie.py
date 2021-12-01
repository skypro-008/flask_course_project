from http import HTTPStatus

from flask_restx import Namespace, Resource

from project.services.items import MoviesService
from project.tools.setup_db import db
from project.views.dto import movie_state_parser

movies_ns = Namespace('movies', validate=True)


@movies_ns.route('/')
class MoviesView(Resource):

    @movies_ns.expect(movie_state_parser)
    @movies_ns.response(int(HTTPStatus.OK), 'OK')
    def get(self):
        """ Get all movies """
        return MoviesService(db.session).get_all_movies(**movie_state_parser.parse_args()), HTTPStatus.OK


@movies_ns.route('/<int:movie_id>')
class MovieView(Resource):

    @movies_ns.response(int(HTTPStatus.OK), 'OK')
    @movies_ns.response(int(HTTPStatus.NOT_FOUND), 'Movie not found')
    def get(self, movie_id: int):
        """ Get movie by id """
        return MoviesService(db.session).get_movie(movie_id), HTTPStatus.OK
