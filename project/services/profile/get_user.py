from project.dao import UserDAO
from project.services import BaseService
from project.services.schemas import UserSchema


class GetUserService(BaseService):
    def execute(self, pk: int) -> dict:
        return UserSchema().dump(UserDAO(self._db_session).get_by_id(pk))
