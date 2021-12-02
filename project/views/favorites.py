from http import HTTPStatus

from flask_restx import Namespace, Resource

from project.services.profile import FavoritesService
from project.views.validators import PageValidator
from project.setup_db import db
from project.utils.auth_decorator import login_required
from project.views.dto import pages_parser

favorites_ns = Namespace("favorites", validate=True)


@favorites_ns.doc(security="Bearer")
@favorites_ns.route("/movies/<int:movie_id>")
class ManageFavoriteView(Resource):
    @favorites_ns.response(int(HTTPStatus.OK), "OK")
    @favorites_ns.response(int(HTTPStatus.NOT_FOUND), "Movie not found")
    @login_required
    def post(self, user_id: int, movie_id: int):
        """Добавить фильм в избранное"""
        FavoritesService(db.session).add(user_id, movie_id)
        return None, HTTPStatus.OK

    @favorites_ns.response(int(HTTPStatus.NO_CONTENT), "Deleted")
    @favorites_ns.response(int(HTTPStatus.NOT_FOUND), "Movie not found")
    @login_required
    def delete(self, user_id: int, movie_id: int):
        """Удалить фильм из избранного"""
        return (
            FavoritesService(db.session).delete(user_id, movie_id),
            HTTPStatus.NO_CONTENT,
        )


@favorites_ns.doc(security="Bearer")
@favorites_ns.route("/movies/")
class FavoritesView(Resource):
    @favorites_ns.expect(pages_parser)
    @favorites_ns.response(int(HTTPStatus.OK), "OK")
    @login_required
    def get(self, user_id: int):
        """Получить список избранных фильмов"""
        return (
            FavoritesService(db.session).get_all(
                user_id=user_id,
                page=PageValidator().load(pages_parser.parse_args()).get("page"),
            ),
            HTTPStatus.OK,
        )
