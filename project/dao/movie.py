from typing import List, Optional

from sqlalchemy import desc

from project.dao import BaseDAO
from project.models import Movie
from project.utils.utils import get_limit_and_offset


class MovieDAO(BaseDAO):
    __model__ = Movie

    def get_all(
        self, page: Optional[int] = None, new: bool = False, **kwargs
    ) -> List[Movie]:
        stmt = self._db_session.query(Movie)
        if new:
            stmt = stmt.order_by(desc(Movie.year))
        if page:
            limit, offset = get_limit_and_offset(page)
            stmt = stmt.limit(limit).offset(offset)
        return stmt.all()
