from project.dao import UserDAO
from project.exceptions import InvalidCredentials
from project.models import User
from project.tools.security import compare_passwords
from project.tools.service import BaseService


class CheckUserCredentialsService(BaseService):

    def execute(self, email: str, password: str) -> User:
        if not (user := UserDAO(self._db_session).get_user_by_email(email)):
            raise InvalidCredentials

        if not compare_passwords(user.password_hash, password):
            raise InvalidCredentials

        return user
