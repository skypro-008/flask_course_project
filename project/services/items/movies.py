from typing import List

from project.dao import MovieDAO
from project.services import ItemServiceBase
from project.tools.exceptions import MovieNotFoundException
from project.tools.schemas import MovieSchema
from project.utils.utils import get_limit_and_offset


class MoviesService(ItemServiceBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dao = MovieDAO(self._db_session)
        self.schema = MovieSchema
        self.not_found_exception = MovieNotFoundException

    def get_all(self, page: int = 1, state: str = None, **kwargs) -> List[dict]:
        limit, offset = get_limit_and_offset(page)
        return self.schema(many=True).dump(self.dao.get_all(limit, offset, new=(state == 'new')))
