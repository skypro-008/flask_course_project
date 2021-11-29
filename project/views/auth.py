from http import HTTPStatus

from flask_restx import Namespace, Resource

from project.exceptions import BaseProjectException
from project.services.auth import RegisterNewUserService
from project.tools.setup_db import db
from project.views.dto import auth_reqparser

auth_ns = Namespace('auth', validate=True)


@auth_ns.route('/register')
class RegisterUser(Resource):

    @auth_ns.expect(auth_reqparser)
    @auth_ns.response(int(HTTPStatus.CREATED), "Created")
    @auth_ns.response(int(HTTPStatus.CONFLICT), "Record already exists")
    @auth_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error")
    def post(self):
        """ Register a new user """
        try:
            RegisterNewUserService(db.session).execute(**auth_reqparser.parse_args())
            return None, HTTPStatus.CREATED
        except BaseProjectException as e:
            return e.to_dict(), HTTPStatus.CONFLICT
