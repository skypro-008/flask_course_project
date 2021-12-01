from http import HTTPStatus

from flask_restx import fields, Namespace, Resource
from jwt import PyJWTError

from project.services.auth import CheckUserCredentialsService, RegisterNewUserService
from project.utils.jwt_token import JwtToken
from project.tools.setup_db import db
from project.views.dto import auth_parser, login_parser

auth_ns = Namespace('auth', validate=True)

tokens = auth_ns.model('Access and Refresh tokens', {
    'access_token': fields.String(required=True),
    'refresh_token': fields.String(required=True)
})


@auth_ns.route('/register')
class RegisterUserView(Resource):

    @auth_ns.expect(auth_parser)
    @auth_ns.response(int(HTTPStatus.CREATED), 'Created')
    @auth_ns.response(int(HTTPStatus.CONFLICT), 'Record already exists')
    @auth_ns.response(int(HTTPStatus.BAD_REQUEST), 'Validation error')
    def post(self):
        """ Register a new user """
        RegisterNewUserService(db.session).execute(**auth_parser.parse_args())
        return None, HTTPStatus.CREATED


@auth_ns.route('/login')
class LoginUserView(Resource):
    @auth_ns.expect(login_parser)
    @auth_ns.response(int(HTTPStatus.OK), 'OK')
    @auth_ns.response(int(HTTPStatus.UNAUTHORIZED), 'Invalid credentials')
    @auth_ns.response(int(HTTPStatus.BAD_REQUEST), 'Validation error')
    def post(self):
        """ Authenticate user and send access, refresh tokens and user_id"""
        return CheckUserCredentialsService(db.session).execute(**login_parser.parse_args()), HTTPStatus.OK

    @auth_ns.expect(tokens)
    @auth_ns.response(int(HTTPStatus.OK), 'Updated', tokens)
    @auth_ns.response(int(HTTPStatus.UNAUTHORIZED), 'Invalid refresh token')
    def put(self):
        """ Update access and refresh tokens. """
        try:
            data = JwtToken.decode_token(auth_ns.payload['refresh_token'])
            return JwtToken(data).get_tokens(), HTTPStatus.OK
        except PyJWTError:
            return {'message': 'Invalid refresh token'}, HTTPStatus.UNAUTHORIZED
