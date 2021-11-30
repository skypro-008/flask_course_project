from http import HTTPStatus

from flask_restx import Namespace, Resource

from project.services.profile import ChangeUserPasswordService, GetUserService, UpdateProfileInfoService
from project.tools.setup_db import db
from project.views.dto import change_password_parser, change_user_info_parser

user_ns = Namespace('user', validate=True)


@user_ns.route('/<int:pk>')
class UserProfileView(Resource):

    @user_ns.response(int(HTTPStatus.OK), 'OK')
    @user_ns.response(int(HTTPStatus.NOT_FOUND), 'User not found')
    def get(self, pk: int):
        """ Get user profile. """
        return GetUserService(db.session).execute(pk)

    @user_ns.expect(change_user_info_parser)
    @user_ns.response(int(HTTPStatus.OK), 'OK')
    @user_ns.response(int(HTTPStatus.NOT_FOUND), 'User or genre not found')
    @user_ns.response(int(HTTPStatus.BAD_REQUEST), 'Validation error')
    def patch(self, pk: int):
        """ Update user info"""
        data = UpdateProfileInfoService(db.session).execute(pk, **change_user_info_parser.parse_args())
        print('#', data, '#')
        return UpdateProfileInfoService(db.session).execute(pk, **change_user_info_parser.parse_args())


@user_ns.route('/<int:pk>/setpassword')
class ChangePasswordView(Resource):
    @user_ns.expect(change_password_parser)
    @user_ns.response(int(HTTPStatus.OK), 'OK')
    @user_ns.response(int(HTTPStatus.BAD_REQUEST), 'Password mismatch')
    @user_ns.response(int(HTTPStatus.NOT_FOUND), 'User not found')
    def put(self, pk: int):
        """ Change user password """
        ChangeUserPasswordService(db.session).execute(pk=pk, **change_password_parser.parse_args())
