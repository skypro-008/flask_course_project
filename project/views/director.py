from http import HTTPStatus

from flask_restx import Namespace, Resource

from project.services.items import DirectorsService
from project.tools.setup_db import db
from project.views.dto import pages_parser

directors_ns = Namespace('directors', validate=True)


@directors_ns.route('/')
class DirectorsView(Resource):

    @directors_ns.expect(pages_parser)
    @directors_ns.response(int(HTTPStatus.OK), 'OK')
    def get(self):
        """ Get all directors """
        return DirectorsService(db.session).get_all(**pages_parser.parse_args()), HTTPStatus.OK


@directors_ns.route('/<int:director_id>')
class DirectorView(Resource):

    @directors_ns.response(int(HTTPStatus.OK), 'OK')
    @directors_ns.response(int(HTTPStatus.NOT_FOUND), 'Director not found')
    def get(self, director_id: int):
        """ Get movie by id """
        return DirectorsService(db.session).get_item(director_id), HTTPStatus.OK
