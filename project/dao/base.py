from abc import ABC, abstractmethod
from typing import Optional, Tuple

from flask import current_app

from project.setup.db.models import Base


class BaseDAO(ABC):
    # TODO: Указать возвращаемые типы
    __model__ = Base

    def __init__(self, db_session):
        self._db_session = db_session

    @abstractmethod
    def get_by_id(self, pk: int):
        return self._db_session.query(self.__model__).filter(self.__model__.id == pk).one_or_none()

    @abstractmethod
    def get_all(self, page: Optional[int] = None):
        stmt = self._db_session.query(self.__model__)
        if page:
            limit, offset = self._get_limit_and_offset(page)
            stmt = stmt.limit(limit).offset(offset)
        return stmt.all()

    @staticmethod
    def _get_limit_and_offset(page: int) -> Tuple[int, int]:
        limit = current_app.config['ITEMS_PER_PAGE']
        offset = 0 if page < 1 else limit * (page - 1)
        return limit, offset
