from typing import List

from project.dao import GenreDAO
from project.errors import NotFoundError
from project.models import Genre
from project.services.base import BaseService


class GenresService(BaseService):
    def __init__(self, db_session):
        super().__init__(db_session)
        self.dao = GenreDAO(db_session)

    def get_item(self, pk: int) -> Genre:
        if not (genre := self.dao.get_by_id(pk)):
            raise NotFoundError('Genre not found')
        return genre

    def get_all(self, page: int = None) -> List[Genre]:
        if page is None:
            return self.dao.get_all()
        else:
            return self.dao.get_all(page=page)
