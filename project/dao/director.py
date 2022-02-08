from typing import List, Optional

from project.dao import BaseDAO
from project.models import Director


class DirectorDAO(BaseDAO):
    __model__ = Director

    def get_by_id(self, pk: int) -> Optional[Director]:
        return super().get_by_id(pk)

    def get_all(self, page: Optional[int] = None, **kwargs) -> List[Director]:
        return super().get_all(page=page, **kwargs)
