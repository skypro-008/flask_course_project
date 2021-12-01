from typing import List

from project.dao import MovieDAO
from project.services import BaseService
from project.tools.exceptions import MovieNotFound
from project.tools.schemas import MovieSchema
from project.utils.utils import get_limit_and_offset


class MoviesService(BaseService):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.movie_dao = MovieDAO(self._db_session)
        self.schema = MovieSchema()

    def get_all_movies(self, state: str = None, page: int = 1) -> List[dict]:
        limit, offset = get_limit_and_offset(page)
        return MovieSchema(many=True).dump(self.movie_dao.get_all(limit, offset, new=state == 'new'))

    def get_movie(self, movie_id: int) -> dict:
        if not self.movie_dao.get_by_id(movie_id):
            raise MovieNotFound
        return MovieSchema().dump(self.movie_dao.get_by_id(movie_id))
