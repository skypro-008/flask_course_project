from typing import List

from project.dao import MovieDAO
from project.exceptions import MovieNotFoundException
from project.services import ItemServiceBase
from project.services.schemas import MovieSchema


class MoviesService(ItemServiceBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dao = MovieDAO(self._db_session)
        self.schema = MovieSchema
        self.not_found_exception = MovieNotFoundException

    def get_all(self, **kwargs) -> List[dict]:
        return self.schema(many=True).dump(
            self.dao.get_all(
                page=kwargs.get('page'), new=(kwargs.get('state') == 'new')
            )
        )
