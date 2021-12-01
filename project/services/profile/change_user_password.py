from project.dao import UserDAO
from project.services import BaseService
from project.tools.exceptions import PasswordsMismatch, UserNotFound
from project.utils.security import generate_password_hash


class ChangeUserPasswordService(BaseService):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_dao = UserDAO(self._db_session)

    def execute(self, pk: int, password_1: str, password_2: str) -> None:
        if password_1 != password_2:
            raise PasswordsMismatch

        if user := self.user_dao.get_by_id(pk):
            self.user_dao.update_user_password(
                user_id=user.id,
                password=generate_password_hash(password_1)
            )
        else:
            raise UserNotFound
