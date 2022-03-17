from typing import List

from project.dao import DirectorDAO
from project.errors import NotFoundError
from project.models import Director
from project.services.base import BaseService


class DirectorsService(BaseService):
    def __init__(self, db_session):
        super().__init__(db_session)
        self.dao = DirectorDAO(db_session)

    def get_all(self, page: int = None) -> List[Director]:
        if page is None:
            return self.dao.get_all()
        else:
            return self.dao.get_all(page=page)

    def get_item(self, pk: int) -> Director:
        if not (director := self.dao.get_by_id(pk)):
            raise NotFoundError('Director not found')
        return director
