from typing import Optional

from sqlalchemy.exc import IntegrityError

from project.exceptions import UserAlreadyExists
from project.models import User
from project.tools.dao import BaseDAO


class UserDAO(BaseDAO):

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self._db_session.query(User).filter(User.email == email).one_or_none()

    def create(self, email: str, password: str) -> User:
        obj = User(email=email, password=password)
        try:
            self._db_session.add(obj)
            self._db_session.commit()
        except IntegrityError:
            raise UserAlreadyExists
        return obj
