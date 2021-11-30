from typing import Optional

from project.models import Genre
from project.tools.dao import BaseDAO


class GenreDAO(BaseDAO):

    def get_genre_by_id(self, pk: int) -> Optional[Genre]:
        return self._db_session.query(Genre).filter(Genre.id == pk).one_or_none()
