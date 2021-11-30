from project.dao import UserDAO
from project.exceptions import UserNotFound
from project.schemas import UserSchema
from project.tools.service import BaseService


class GetUserService(BaseService):

    def execute(self, pk: int) -> dict:
        if user := UserDAO(self._db_session).get_user_by_id(pk):
            return UserSchema().dump(user)
        raise UserNotFound
