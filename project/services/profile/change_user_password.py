from project.dao import UserDAO
from project.exceptions import PasswordsMismatch
from project.services import BaseService
from project.utils.security import generate_password_hash


class ChangeUserPasswordService(BaseService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_dao = UserDAO(self._db_session)

    def execute(self, user_id: int, password_1: str, password_2: str) -> None:
        if password_1 != password_2:
            raise PasswordsMismatch

        self.user_dao.update_user_password(
            user_id=user_id, password=generate_password_hash(password_1)
        )
