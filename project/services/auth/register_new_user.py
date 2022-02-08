from project.dao import UserDAO
from project.services import BaseService
from project.utils.security import generate_password_hash


class RegisterNewUserService(BaseService):
    def execute(self, email: str, password: str) -> None:
        UserDAO(self._db_session).create(
            email=email, password=generate_password_hash(password)
        )
