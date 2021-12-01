from typing import List, Optional, Type, Union

from flask_sqlalchemy.model import Model
from sqlalchemy.orm.scoping import scoped_session

from project.models import BaseMixin


class BaseDAO:
    __model__: Type[Union[Model, BaseMixin]] = NotImplemented

    def __init__(self, session: scoped_session):
        self._db_session = session

    def get_by_id(self, pk: int) -> Optional[Union[Model, BaseMixin]]:
        return self._db_session.query(self.__model__).filter(self.__model__.id == pk).one_or_none()

    def get_all(self, limit: int, offset: int, **kwargs) -> List[Model]:
        return self._db_session.query(self.__model__).limit(limit).offset(offset).all()
