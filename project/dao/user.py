from typing import Optional

from sqlalchemy.exc import IntegrityError

from project.tools.exceptions import UserAlreadyExists, UserNotFound
from project.models import User
from project.tools.schemas import UserSchema
from project.dao import BaseDAO


class UserDAO(BaseDAO):

    def update_user_info(self, user_id: int, **kwargs) -> User:

        self._db_session.query(User).filter(User.id == user_id).update(
            UserSchema().load(kwargs, partial=('email', 'password'))
        )
        self._db_session.commit()

        if user := self._db_session.query(User).filter(User.id == user_id).one_or_none():
            return user
        raise UserNotFound

    def update_user_password(self, user_id: int, password: str) -> None:
        if user := self._db_session.query(User).filter(User.id == user_id).one_or_none():
            user.password = password
            self._db_session.add(user)
            self._db_session.commit()
        else:
            raise UserNotFound

    def get_user_by_id(self, pk: int) -> Optional[User]:
        return self._db_session.query(User).filter(User.id == pk).one_or_none()

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self._db_session.query(User).filter(User.email == email).one_or_none()

    def create(self, email: str, password: str) -> User:
        obj = User(**UserSchema().load({'email': email, 'password': password}))
        try:
            self._db_session.add(obj)
            self._db_session.commit()
        except IntegrityError:
            raise UserAlreadyExists
        return obj
