from typing import List, Optional

from flask_sqlalchemy import BaseQuery
from sqlalchemy import desc

from project.dao.base import BaseDAO
from project.models import Director, Genre, Movie


class GenreDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorDAO(BaseDAO[Director]):
    __model__ = Director


class MovieDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all(self, page: Optional[int] = None, new: bool = False) -> List[Movie]:
        stmt: BaseQuery = self._db_session.query(Movie)
        if new:
            stmt: BaseQuery = stmt.order_by(desc(Movie.year))  # type: ignore[no-redef]
        if page:
            return stmt.paginate(page=page, per_page=self._items_per_page).items
        return stmt.all()
