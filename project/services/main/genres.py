from typing import List

from project.dao import GenreDAO
from project.models import Genre
from project.services.base import BaseService


class GenresService(BaseService):
    def __init__(self, db_session) -> None:
        super().__init__(db_session)
        self.dao = GenreDAO(db_session)

    def get_item(self, pk: int) -> Genre:
        return self.dao.get_by_id(pk)

    def get_all(self, page: int = None) -> List[Genre]:
        return self.dao.get_all(page=page)
