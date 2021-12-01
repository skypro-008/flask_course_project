from typing import List

from sqlalchemy import desc

from project.dao import BaseDAO
from project.models import Movie


class MovieDAO(BaseDAO):
    __model__ = Movie

    def get_all(self, limit: int, offset: int, new: bool = False) -> List[Movie]:
        stmt = self._db_session.query(Movie)
        if new:
            stmt = stmt.order_by(desc(Movie.year))
        return stmt.limit(limit).offset(offset).all()
