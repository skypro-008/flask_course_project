from flask import url_for
from flask_restx import Namespace, Resource

from project.services.auth import AuthService
from project.setup.api.models import error, tokens
from project.setup.api.parsers import auth_parser, tokens_parser
from project.setup.db import db

api = Namespace('auth')


@api.route('/register')
class RegisterUserView(Resource):
    @api.expect(auth_parser)
    @api.response(code=201, description='Created', headers={'Location': 'The URL of a newly created user'})
    @api.response(code=400, description='Bad request', model=error)
    @api.response(code=409, description='Record already exists', model=error)
    def post(self):
        """
        Register a new user.
        """
        AuthService(db.session).register_user(**auth_parser.parse_args())
        return None, 201, {'Location': url_for('user_user_profile_view')}


@api.route('/login')
@api.response(code=401, description='Invalid credentials', model=error)
class LoginUserView(Resource):
    @api.expect(auth_parser)
    @api.marshal_with(tokens, code=200, description='OK')
    @api.response(code=400, description='Bad request', model=error)
    def post(self):
        """
        Authenticate user and send access and refresh tokens.
        """
        return AuthService(db.session).check_user_credentials(**auth_parser.parse_args())

    @api.expect(tokens_parser)
    @api.marshal_with(tokens, code=200, description='Updated')
    @api.response(code=401, description='Invalid refresh token', model=error)
    def put(self):
        """
        Update access and refresh tokens.
        """
        return AuthService(db.session).update_tokens(tokens_parser.parse_args()['refresh_token'])
