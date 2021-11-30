from http import HTTPStatus

from flask_restx import Namespace, Resource

from project.services.profile import GetUserService
from project.tools.setup_db import db

user_ns = Namespace('user', validate=True)


@user_ns.route('/<int:pk>')
class UserProfileView(Resource):

    @user_ns.response(int(HTTPStatus.OK), 'OK')
    @user_ns.response(int(HTTPStatus.NOT_FOUND), 'User not found')
    def get(self, pk: int):
        """ Get user profile. """
        return GetUserService(db.session).execute(pk)
