from typing import Optional

from sqlalchemy.exc import IntegrityError

from project.exceptions import UserAlreadyExists
from project.models import User
from project.tools.dao import BaseDAO
from project.tools.enums import UserRole


class UserDAO(BaseDAO):

    def create(
        self, email: str, password_hash: str, role: UserRole, name: Optional[str] = None, surname: Optional[str] = None
    ) -> User:
        obj = User(
            email=email,
            password_hash=password_hash,
            role=role,
            name=name,
            surname=surname
        )
        try:
            self._db_session.add(obj)
            self._db_session.commit()
        except IntegrityError:
            raise UserAlreadyExists
        return obj
