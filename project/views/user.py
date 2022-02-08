from http import HTTPStatus

from flask_restx import Namespace, Resource, fields

from project.services.profile import (ChangeUserPasswordService,
                                      GetUserService, UpdateProfileInfoService)
from project.setup_db import db
from project.utils.auth_decorator import login_required
from project.views.dto import change_password_parser, change_user_info_parser

user_ns = Namespace('user', validate=True)

user_profile = user_ns.model(
    'Профиль пользователя',
    {
        'id': fields.Integer(required=True),
        'email': fields.String(required=True),
        'name': fields.String,
        'surname': fields.String,
        'favourite_genre': fields.Integer,
    },
)


@user_ns.doc(security='Bearer')
@user_ns.route('/')
class UserProfileView(Resource):
    @user_ns.response(int(HTTPStatus.OK), 'OK', user_profile)
    @user_ns.marshal_with(user_profile)
    @login_required
    def get(self, user_id: int):
        """Получить профиль пользователя"""
        return GetUserService(db.session).execute(user_id)

    @user_ns.expect(change_user_info_parser)
    @user_ns.response(int(HTTPStatus.OK), 'OK', user_profile)
    @user_ns.response(int(HTTPStatus.NOT_FOUND), 'Genre not found')
    @user_ns.response(int(HTTPStatus.BAD_REQUEST), 'Validation error')
    @user_ns.marshal_with(user_profile)
    @login_required
    def patch(self, user_id: int):
        """Обновить профиль пользователя"""
        return UpdateProfileInfoService(db.session).execute(
            user_id=user_id, **change_user_info_parser.parse_args()
        )


@user_ns.doc(security='Bearer')
@user_ns.route('/password')
class ChangePasswordView(Resource):
    @user_ns.expect(change_password_parser)
    @user_ns.response(int(HTTPStatus.OK), 'OK')
    @user_ns.response(int(HTTPStatus.BAD_REQUEST), 'Password mismatch')
    @login_required
    def put(self, user_id: int):
        """Обновить пароль пользователя"""
        ChangeUserPasswordService(db.session).execute(
            user_id=user_id, **change_password_parser.parse_args()
        )
        return None, HTTPStatus.OK
