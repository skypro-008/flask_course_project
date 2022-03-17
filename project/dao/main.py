from typing import List, Optional

from sqlalchemy import desc

from project.dao.base import BaseDAO
from project.models import Director, Genre, Movie


class GenreDAO(BaseDAO):
    __model__ = Genre

    def get_by_id(self, pk: int) -> Optional[Genre]:
        return super().get_by_id(pk)

    def get_all(self, page: Optional[int] = None) -> List[Genre]:
        return super().get_all(page=page)


class DirectorDAO(BaseDAO):
    __model__ = Director

    def get_by_id(self, pk: int) -> Optional[Director]:
        return super().get_by_id(pk)

    def get_all(self, page: Optional[int] = None) -> List[Director]:
        return super().get_all(page=page)


class MovieDAO(BaseDAO):
    __model__ = Movie

    def get_by_id(self, pk: int) -> Optional[Movie]:
        return super().get_by_id(pk)

    def get_all(self, page: Optional[int] = None, new: bool = False) -> List[Movie]:
        stmt = self._db_session.query(Movie)
        if new:
            stmt = stmt.order_by(desc(Movie.year))
        if page:
            limit, offset = self._get_limit_and_offset(page)
            stmt = stmt.limit(limit).offset(offset)
        return stmt.all()
