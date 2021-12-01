from http import HTTPStatus

from flask_restx import Namespace, Resource

from project.services.items import GenresService
from project.tools.setup_db import db
from project.views.dto import pages_parser

genres_ns = Namespace('genres', validate=True)


@genres_ns.route('/')
class GenresView(Resource):

    @genres_ns.expect(pages_parser)
    @genres_ns.response(int(HTTPStatus.OK), 'OK')
    def get(self):
        """ Get all genres """
        return GenresService(db.session).get_all(**pages_parser.parse_args()), HTTPStatus.OK


@genres_ns.route('/<int:genre_id>')
class GenreView(Resource):

    @genres_ns.response(int(HTTPStatus.OK), 'OK')
    @genres_ns.response(int(HTTPStatus.NOT_FOUND), 'Genre not found')
    def get(self, genre_id: int):
        """ Get genre by id """
        return GenresService(db.session).get_item(genre_id), HTTPStatus.OK
