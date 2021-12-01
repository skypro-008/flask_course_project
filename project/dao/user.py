from contextlib import suppress
from typing import List, Optional

from sqlalchemy.exc import IntegrityError

from project.dao import BaseDAO
from project.models import Movie, User
from project.tools.exceptions import UserAlreadyExists
from project.tools.schemas import UserSchema


class UserDAO(BaseDAO):
    __model__ = User

    def add_movie_to_favorites(self, user_id: int, movie_id: int):
        user = User.query.get(user_id)
        movie = Movie.query.get(movie_id)

        user.favorites.append(movie)
        self._db_session.commit()

    def remote_from_favorites(self, user_id: int, movie_id: int):
        user = User.query.get(user_id)
        movie = Movie.query.get(movie_id)

        with suppress(ValueError):
            user.favorites.remove(movie)
            self._db_session.commit()

    def get_favorites(self, user_id: int) -> List[Movie]:
        user = self._db_session.query(User).filter(User.id == user_id).one()
        return user.favorites

    def update_user_info(self, user_id: int, **kwargs) -> User:
        self._db_session.query(User).filter(User.id == user_id).update(
            UserSchema().load(kwargs, partial=('email', 'password'))
        )
        self._db_session.commit()

        return User.query.get(user_id)

    def update_user_password(self, user_id: int, password: str) -> None:
        self._db_session.query(User).filter(User.id == user_id).update({'password': password})
        self._db_session.commit()

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
