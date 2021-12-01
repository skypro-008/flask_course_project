from http import HTTPStatus

from flask_restx import Namespace, Resource

from project.services.profile import ChangeUserPasswordService, FavoritesService, GetUserService, \
    UpdateProfileInfoService
from project.tools.setup_db import db
from project.utils.auth import login_required
from project.views.dto import change_password_parser, change_user_info_parser, pages_parser

user_ns = Namespace('user', validate=True)


@user_ns.doc(security='Bearer')
@user_ns.route('/<int:pk>')
class UserProfileView(Resource):

    @user_ns.response(int(HTTPStatus.OK), 'OK')
    @login_required
    def get(self, pk: int):
        """ Get user profile. """
        return GetUserService(db.session).execute(pk)

    @user_ns.expect(change_user_info_parser)
    @user_ns.response(int(HTTPStatus.OK), 'OK')
    @user_ns.response(int(HTTPStatus.NOT_FOUND), 'Genre not found')
    @user_ns.response(int(HTTPStatus.BAD_REQUEST), 'Validation error')
    def patch(self, pk: int):
        """ Update user info"""
        data = UpdateProfileInfoService(db.session).execute(pk, **change_user_info_parser.parse_args())
        print('#', data, '#')
        return UpdateProfileInfoService(db.session).execute(pk, **change_user_info_parser.parse_args())


@user_ns.doc(security='Bearer')
@user_ns.route('/<int:pk>/setpassword')
class ChangePasswordView(Resource):
    @user_ns.expect(change_password_parser)
    @user_ns.response(int(HTTPStatus.OK), 'OK')
    @user_ns.response(int(HTTPStatus.BAD_REQUEST), 'Password mismatch')
    def put(self, pk: int):
        """ Change user password """
        ChangeUserPasswordService(db.session).execute(pk=pk, **change_password_parser.parse_args())
        return None, HTTPStatus.OK


@user_ns.doc(security='Bearer')
@user_ns.route('/<int:user_id>/favorites/<int:movie_id>')
class ManageFavoriteView(Resource):

    @user_ns.response(int(HTTPStatus.OK), 'OK')
    @user_ns.response(int(HTTPStatus.NOT_FOUND), 'Movie not found')
    def post(self, user_id: int, movie_id: int):
        FavoritesService(db.session).add(user_id, movie_id)
        return None, HTTPStatus.OK

    @user_ns.response(int(HTTPStatus.NO_CONTENT), 'Deleted')
    @user_ns.response(int(HTTPStatus.NOT_FOUND), 'Movie not found')
    def delete(self, user_id: int, movie_id: int):
        return FavoritesService(db.session).delete(user_id, movie_id), HTTPStatus.NO_CONTENT


@user_ns.doc(security='Bearer')
@user_ns.route('/<int:user_id>/favorites')
class FavoritesView(Resource):

    @user_ns.expect(pages_parser)
    @user_ns.response(int(HTTPStatus.OK), 'OK')
    def get(self, user_id: int):
        return FavoritesService(db.session).get_all(user_id, **pages_parser.parse_args()), HTTPStatus.OK
