from project.dao import UserDAO
from project.services.schemas import UserSchema
from project.tools.security import generate_password_hash
from project.tools.service import BaseService


class RegisterNewUserService(BaseService):

    def execute(self, email: str, password: str) -> None:
        UserDAO(self._db_session).create(**UserSchema().load({
            'email': email,
            'password': generate_password_hash(password),
        }))
