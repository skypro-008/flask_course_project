from flask_restx import Namespace, Resource

from project.services.main import MoviesService
from project.setup.api.models import error, movie
from project.setup.api.parsers import movie_state_and_page_parser
from project.setup.db import db

api = Namespace('movies')


@api.route('/')
class MoviesView(Resource):
    @api.expect(movie_state_and_page_parser)
    @api.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all movies.
        """
        return MoviesService(db.session).get_all(**movie_state_and_page_parser.parse_args())


@api.route('/<int:movie_id>')
class MovieView(Resource):
    @api.response(404, 'Not Found', error)
    @api.marshal_with(movie, code=200, description='OK')
    def get(self, movie_id: int):
        """
        Get movie by id.
        """
        return MoviesService(db.session).get_item(movie_id)
