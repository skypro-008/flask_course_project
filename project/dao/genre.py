from typing import List, Optional

from project.dao import BaseDAO
from project.models import Genre


class GenreDAO(BaseDAO):
    __model__ = Genre

    def get_by_id(self, pk: int) -> Optional[Genre]:
        return super().get_by_id(pk)

    def get_all(self, page: Optional[int] = None, **kwargs) -> List[Genre]:
        return super().get_all(page=page, **kwargs)
