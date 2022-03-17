from typing import List

from project.dao import MovieDAO
from project.errors import NotFoundError
from project.models import Movie
from project.services.base import BaseService


class MoviesService(BaseService):
    def __init__(self, db_session):
        super().__init__(db_session)
        self.dao = MovieDAO(db_session)

    def get_all(self, state: str = None, page: int = None) -> List[Movie]:
        return self.dao.get_all(page=page, new=(state == 'new'))

    def get_item(self, pk: int) -> Movie:
        if not (movie := self.dao.get_by_id(pk)):
            raise NotFoundError('Movie not found')
        return movie
