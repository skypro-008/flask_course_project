from http import HTTPStatus

from flask_restx import Namespace, Resource

from project.services.profile import ChangeUserPasswordService, FavoritesService, GetUserService, \
    UpdateProfileInfoService
from project.tools.setup_db import db
from project.utils.auth import login_required
from project.views.dto import change_password_parser, change_user_info_parser, pages_parser

user_ns = Namespace('user', validate=True)


@user_ns.doc(security='Bearer')
@user_ns.route('/')
class UserProfileView(Resource):

    @user_ns.response(int(HTTPStatus.OK), 'OK')
    @login_required
    def get(self, user_id: int):
        """ Get user profile. """
        return GetUserService(db.session).execute(user_id)

    @user_ns.expect(change_user_info_parser)
    @user_ns.response(int(HTTPStatus.OK), 'OK')
    @user_ns.response(int(HTTPStatus.NOT_FOUND), 'Genre not found')
    @user_ns.response(int(HTTPStatus.BAD_REQUEST), 'Validation error')
    @login_required
    def patch(self, user_id: int):
        """ Update user info"""
        return UpdateProfileInfoService(db.session).execute(user_id, **change_user_info_parser.parse_args())


@user_ns.doc(security='Bearer')
@user_ns.route('/password')
class ChangePasswordView(Resource):
    @user_ns.expect(change_password_parser)
    @user_ns.response(int(HTTPStatus.OK), 'OK')
    @user_ns.response(int(HTTPStatus.BAD_REQUEST), 'Password mismatch')
    @login_required
    def put(self, user_id: int):
        """ Change user password """
        ChangeUserPasswordService(db.session).execute(user_id=user_id, **change_password_parser.parse_args())
        return None, HTTPStatus.OK


