from flask_restx import Namespace, Resource

from project.services.main import DirectorsService
from project.setup.api.models import director, error
from project.setup.api.parsers import page_parser
from project.setup.db import db

api = Namespace('directors')


@api.route('/')
class DirectorsView(Resource):
    @api.expect(page_parser)
    @api.marshal_with(director, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all directors.
        """
        return DirectorsService(db.session).get_all(**page_parser.parse_args())


@api.route('/<int:director_id>/')
class DirectorView(Resource):
    @api.response(404, 'Not Found', error)
    @api.marshal_with(director, code=200, description='OK')
    def get(self, director_id: int):
        """
        Get director by id
        """
        return DirectorsService(db.session).get_item(director_id)
