from typing import List, Optional, Type, Union

from flask_sqlalchemy.model import Model
from sqlalchemy.orm.scoping import scoped_session

from project.models import BaseMixin
from project.utils.utils import get_limit_and_offset


class BaseDAO:
    __model__: Type[Union[Model, BaseMixin]] = NotImplemented

    def __init__(self, session: scoped_session):
        self._db_session = session

    def get_by_id(self, pk: int) -> Optional[Union[Model, BaseMixin]]:
        return (
            self._db_session.query(self.__model__)
            .filter(self.__model__.id == pk)
            .one_or_none()
        )

    def get_all(self, page: Optional[int] = None, **kwargs) -> List[Model]:
        stmt = self._db_session.query(self.__model__)
        if page:
            limit, offset = get_limit_and_offset(page)
            stmt = stmt.limit(limit).offset(offset)
        return stmt.all()
