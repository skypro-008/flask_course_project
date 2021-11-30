from typing import Dict

from project.dao import UserDAO
from project.tools.exceptions import InvalidCredentials
from project.tools.schemas import UserSchema
from project.utils.jwt_token import JwtToken
from project.utils.security import compare_passwords
from project.services import BaseService


class CheckUserCredentialsService(BaseService):

    def execute(self, email: str, password: str) -> Dict[str, str]:
        if not (user := UserDAO(self._db_session).get_user_by_email(email)):
            raise InvalidCredentials

        if not compare_passwords(user.password, password):
            raise InvalidCredentials

        return JwtToken(UserSchema().dump(user)).get_tokens()
