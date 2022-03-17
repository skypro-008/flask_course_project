from typing import List

from project.dao.director import DirectorDAO
from project.exceptions import DirectorNotFoundException
from project.models import Director
from project.services import ItemServiceBase


class DirectorsService(ItemServiceBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dao = DirectorDAO(self._db_session)

    def get_all(self, page: int = None) -> List[Director]:
        if page is None:
            return self.dao.get_all()
        else:
            return self.dao.get_all(page=page)

    def get_item(self, pk: int) -> Director:
        if not (director := self.dao.get_by_id(pk)):
            raise DirectorNotFoundException
        return director
