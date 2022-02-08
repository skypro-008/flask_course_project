from typing import List, Type

from marshmallow import Schema
from sqlalchemy.orm.scoping import scoped_session

from project.dao import BaseDAO
from project.exceptions import ItemNotFoundException
from project.services.schemas import BaseSchema


class BaseService:
    def __init__(self, session: scoped_session):
        self._db_session = session


class ItemServiceBase(BaseService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dao: BaseDAO = NotImplemented
        self.schema: Type[Schema] = BaseSchema
        self.not_found_exception: Type[ItemNotFoundException] = ItemNotFoundException

    def get_item(self, pk: int) -> dict:
        if not self.dao.get_by_id(pk):
            raise self.not_found_exception
        return self.schema().dump(self.dao.get_by_id(pk))

    def get_all(self, **kwargs) -> List[dict]:
        return self.schema(many=True).dump(self.dao.get_all(page=kwargs.get('page')))
