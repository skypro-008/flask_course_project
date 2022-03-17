from flask_restx import Namespace, Resource

from project.services.main import GenresService
from project.setup.api.models import error, genre
from project.setup.api.parsers import page_parser
from project.setup.db import db

api = Namespace('genres')


@api.route('/')
class GenresView(Resource):
    @api.expect(page_parser)
    @api.marshal_with(genre, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all genres.
        """
        return GenresService(db.session).get_all(**page_parser.parse_args())


@api.route('/<int:genre_id>')
class GenreView(Resource):
    @api.response(404, 'Not Found', error)
    @api.marshal_with(genre, code=200, description='OK')
    def get(self, genre_id: int):
        """
        Get genre by id.
        """
        return GenresService(db.session).get_item(genre_id)
