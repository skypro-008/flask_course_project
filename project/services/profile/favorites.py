from typing import Any, Dict, List

from project.dao import MovieDAO, UserDAO
from project.services import BaseService
from project.tools.exceptions import MovieNotFoundException, UserNotFoundException
from project.tools.schemas import MovieSchema
from project.utils.utils import get_limit_and_offset


class FavoritesService(BaseService):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_dao = UserDAO(self._db_session)
        self.movie_dao = MovieDAO(self._db_session)
        self.schema = MovieSchema(many=True)

    def _check_exists(self, user_id: int, movie_id: int) -> None:
        if not self.user_dao.get_by_id(user_id):
            raise UserNotFoundException

        if not self.movie_dao.get_by_id(movie_id):
            raise MovieNotFoundException

    def add(self, user_id: int, movie_id: int) -> None:
        self._check_exists(user_id, movie_id)
        self.user_dao.add_movie_to_favorites(user_id, movie_id)

    def delete(self, user_id: int, movie_id: int):
        self._check_exists(user_id, movie_id)
        self.user_dao.remote_from_favorites(user_id, movie_id)

    def get_all(self, user_id: int, page: int) -> List[Dict[str, Any]]:
        if not self.user_dao.get_by_id(user_id):
            raise UserNotFoundException

        limit, offset = get_limit_and_offset(page)
        return self.schema.dump(self.user_dao.get_favorites(user_id, limit, offset))
