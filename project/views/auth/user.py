from flask_restx import Namespace, Resource

from project.services.auth import AuthService
from project.setup.api.models import error, user_profile
from project.setup.api.parsers import change_password_parser, change_user_info_parser
from project.setup.db import db
from project.utils.auth_decorator import login_required

api = Namespace('user')


@api.doc(security='Bearer')
@api.response(code=401, description='Authorization needed', model=error)
@api.response(code=404, description='Bad request', model=error)
@api.route('/')
class UserProfileView(Resource):

    @api.marshal_with(user_profile, code=200, description='OK')
    @login_required
    def get(self, user_id: int):
        """
        Получить профиль пользователя.
        """
        return AuthService(db.session).get_user_profile(user_id)

    @api.expect(change_user_info_parser)
    @api.marshal_with(user_profile, code=200, description='OK')
    @api.response(code=404, description='Genre not exists', model=error)
    @login_required
    def patch(self, user_id: int):
        """
        Обновляет профиль пользователя (имя, фамилию, любимый жанр).
        """
        return AuthService(db.session).update_user_profile(user_id=user_id, **change_user_info_parser.parse_args())


@api.doc(security='Bearer')
@api.response(code=401, description='Authorization needed', model=error)
@api.response(code=404, description='Bad request', model=error)
@api.route('/password')
class ChangePasswordView(Resource):

    @api.expect(change_password_parser)
    @api.response(code=200, description='Ok')
    @login_required
    def put(self, user_id: int):
        """
        Обновить пароль пользователя.
        """
        AuthService(db.session).update_user_password(user_id=user_id, **change_password_parser.parse_args())
        return None, 200
