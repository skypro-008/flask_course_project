from project.dao import UserDAO
from project.tools.exceptions import PasswordsMismatch
from project.utils.security import generate_password_hash
from project.services import BaseService


class ChangeUserPasswordService(BaseService):

    def execute(self, pk: int, password_1: str, password_2: str) -> None:
        if password_1 != password_2:
            raise PasswordsMismatch

        UserDAO(self._db_session).update_user_password(
            user_id=pk,
            password=generate_password_hash(password_1)
        )
