from project.dao import UserDAO
from project.tools.security import generate_password_hash
from project.tools.service import BaseService


class RegisterNewUserService(BaseService):

    def execute(self, email: str, password: str) -> None:
        UserDAO(self._db_session).create(
            email=email,
            password=generate_password_hash(password)
        )
