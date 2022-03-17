from typing import List

from project.dao import GenreDAO
from project.exceptions import GenreNotFoundException
from project.models import Genre
from project.services import ItemServiceBase


class GenresService(ItemServiceBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dao = GenreDAO(self._db_session)

    def get_item(self, pk: int) -> Genre:
        if not (genre := self.dao.get_by_id(pk)):
            raise GenreNotFoundException
        return genre

    def get_all(self, page: int = None) -> List[Genre]:
        if page is None:
            return self.dao.get_all()
        else:
            return self.dao.get_all(page=page)
