from flask_restx import Namespace, Resource

from project.services.main import MoviesService
from project.setup.api.models import movie
from project.setup.api.parsers import page_parser
from project.setup.db import db
from project.utils.auth_decorator import login_required

api = Namespace('favorites')


@api.doc(security='Bearer')
@api.response(401, 'Auth required')
@api.route('/movies/')
class FavoritesView(Resource):

    @api.expect(page_parser)
    @api.marshal_with(movie, as_list=True, code=200, description='OK')
    @login_required
    def get(self, user_id: int):
        """
        Получить список избранных фильмов.
        """
        return MoviesService(db.session).get_favorites(user_id, **page_parser.parse_args())


@api.doc(security='Bearer')
@api.response(401, 'Auth required')
@api.response(404, 'Movie not found')
@api.route('/movies/<int:movie_id>')
class ManageFavoriteView(Resource):

    @api.response(200, 'OK')
    @login_required
    def post(self, user_id: int, movie_id: int):
        """
        Добавить фильм в избранное.
        """
        MoviesService(db.session).append_favorites(user_id, movie_id)
        return None, 200

    @api.response(204, 'Deleted')
    @login_required
    def delete(self, user_id: int, movie_id: int):
        """
        Удалить фильм из избранного
        """
        MoviesService(db.session).remove_from_favorites(user_id, movie_id)
        return None, 204
