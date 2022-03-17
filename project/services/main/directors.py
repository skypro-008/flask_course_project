from typing import List

from project.dao import DirectorDAO
from project.models import Director
from project.services.base import BaseService


class DirectorsService(BaseService):
    def __init__(self, db_session) -> None:
        super().__init__(db_session)
        self.dao = DirectorDAO(db_session)

    def get_all(self, page: int = None) -> List[Director]:
        return self.dao.get_all(page=page)

    def get_item(self, pk: int) -> Director:
        return self.dao.get_by_id(pk)
