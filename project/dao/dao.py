from __future__ import annotations

from typing import Optional, Type

from sqlalchemy.orm.scoping import scoped_session

from project.utils.utils import get_limit_and_offset


class BaseDAO:
    __model__: Type[BaseDAO] = NotImplemented
    id = 0

    def __init__(self, session: scoped_session):
        self._db_session = session

    def get_by_id(self, pk: int):
        return (
            self._db_session.query(self.__model__)
                .filter(self.__model__.id == pk)
                .one_or_none()
        )

    def get_all(self, page: Optional[int] = None, **kwargs):
        stmt = self._db_session.query(self.__model__)
        if page:
            limit, offset = get_limit_and_offset(page)
            stmt = stmt.limit(limit).offset(offset)
        return stmt.all()
