from project.dao.schemas import UserSchema
from project.models import User
from project.tools.dao import BaseDAO


class UserDAO(BaseDAO):

    def create(self, **data) -> User:
        obj = UserSchema().load(data)
        self._db_session.add(obj)
        self._db_session.commit()
        return obj
