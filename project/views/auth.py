# from http import HTTPStatus
#
# from flask_restx import Namespace, Resource, fields
#
# from project.services.auth import (CheckUserCredentialsService,
#                                    RegisterNewUserService)
# from project.services.auth.update_token import UpdateTokenService
# from project.setup_db import db
# from project.views.dto import auth_parser
# from project.views.validators import CredentialsValidator, TokenValidator
#
# auth_ns = Namespace('auth', validate=True)
#
# tokens = auth_ns.model(
#     'Access и Refresh токены',
#     {
#         'access_token': fields.String(required=True),
#         'refresh_token': fields.String(required=True),
#     },
# )
#
#
# @auth_ns.route('/register')
# class RegisterUserView(Resource):
#     @auth_ns.expect(auth_parser)
#     @auth_ns.response(int(HTTPStatus.CREATED), 'Created')
#     @auth_ns.response(int(HTTPStatus.CONFLICT), 'Record already exists')
#     @auth_ns.response(int(HTTPStatus.BAD_REQUEST), 'Validation error')
#     def post(self):
#         """Register a new user"""
#         RegisterNewUserService(db.session).execute(
#             **CredentialsValidator().load(auth_parser.parse_args())
#         )
#         return None, HTTPStatus.CREATED
#
#
# @auth_ns.route('/login')
# class LoginUserView(Resource):
#     @auth_ns.expect(auth_parser)
#     @auth_ns.response(int(HTTPStatus.OK), 'OK', tokens)
#     @auth_ns.response(int(HTTPStatus.UNAUTHORIZED), 'Invalid credentials')
#     @auth_ns.response(int(HTTPStatus.BAD_REQUEST), 'Validation error')
#     def post(self):
#         """Authenticate user and send access and refresh tokens"""
#         return (
#             CheckUserCredentialsService(db.session).execute(
#                 **CredentialsValidator().load(auth_parser.parse_args())
#             ),
#             HTTPStatus.OK,
#         )
#
#     @auth_ns.expect(tokens)
#     @auth_ns.response(int(HTTPStatus.OK), 'Updated', tokens)
#     @auth_ns.response(int(HTTPStatus.UNAUTHORIZED), 'Invalid refresh token')
#     def put(self):
#         """Update access and refresh tokens."""
#         return UpdateTokenService(db.session).execute(
#             refresh_token=TokenValidator().load(auth_ns.payload)['refresh_token']
#         )
