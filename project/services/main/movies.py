from typing import List, Optional

from project.dao import MovieDAO, UserDAO
from project.models import Movie
from project.services.base import BaseService


class MoviesService(BaseService):
    def __init__(self, db_session) -> None:
        super().__init__(db_session)
        self._movie_dao = MovieDAO(db_session)
        self._user_dao = UserDAO(db_session)

    def get_item(self, pk: int) -> Movie:
        return self._movie_dao.get_by_id(pk)

    def get_all(self, state: str = None, page: Optional[int] = None) -> List[Movie]:
        return self._movie_dao.get_all(page=page, new=(state == 'new'))

    def get_favorites(self, user_id: int, page: Optional[int] = None) -> List[Movie]:
        return self._user_dao.get_favorite_moveis(user_id, page)

    def append_favorites(self, user_id: int, movie_id: int) -> None:
        self._user_dao.add_movie_to_favorites(user_id, movie_id)

    def remove_from_favorites(self, user_id: int, movie_id: int) -> None:
        self._user_dao.remote_movie_from_favorites(user_id, movie_id)
