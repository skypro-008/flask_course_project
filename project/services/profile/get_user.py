from project.dao import UserDAO
from project.tools.exceptions import UserNotFoundException
from project.tools.schemas import UserSchema
from project.services import BaseService


class GetUserService(BaseService):

    def execute(self, pk: int) -> dict:
        if user := UserDAO(self._db_session).get_by_id(pk):
            return UserSchema().dump(user)
        raise UserNotFoundException
