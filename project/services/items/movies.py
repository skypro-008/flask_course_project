from typing import List

from project.dao import MovieDAO
from project.exceptions import MovieNotFoundException
from project.models import Movie
from project.services import ItemServiceBase
from project.services.schemas import MovieSchema


class MoviesService(ItemServiceBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dao = MovieDAO(self._db_session)
        self.schema = MovieSchema
        self.not_found_exception = MovieNotFoundException

    def get_all(self, state: str = None, page: int = None) -> List[Movie]:
        return self.dao.get_all(page=page, new=(state == 'new'))

    def get_item(self, pk: int) -> Movie:
        if not (movie := self.dao.get_by_id(pk)):
            raise MovieNotFoundException
        return movie
