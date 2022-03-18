from contextlib import suppress
from typing import List, Optional, Tuple

from sqlalchemy.exc import IntegrityError

from project.dao.base import BaseDAO
from project.errors import ConflictError
from project.models import Movie, User


class UserDAO(BaseDAO[User]):
    __model__ = User

    def create(self, email: str, password: str) -> User:
        obj = User(email=email, password=password)
        try:
            self._db_session.add(obj)
            self._db_session.commit()
        except IntegrityError:
            raise ConflictError('User with this email already exists. Choose the diffrent email address.')
        return obj

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self._db_session.query(User).filter(User.email == email).one_or_none()

    def update(self, user_id: int, **kwargs) -> User:
        self._db_session.query(User).filter(User.id == user_id).update(kwargs)
        self._db_session.commit()
        return self.get_by_id(user_id)

    def update_password(self, user_id: int, password: str) -> None:
        self._db_session.query(User).filter(User.id == user_id).update({
            'password': password
        })
        self._db_session.commit()

    def __get_limit_and_offset(self, page: int) -> Tuple[int, int]:
        limit = self._items_per_page
        offset = 0 if page < 1 else limit * (page - 1)
        return limit, offset

    def get_favorite_moveis(self, user_id: int, page: Optional[int] = None) -> List[Movie]:
        user = self.get_by_id(user_id)
        if page:
            limit, offset = self.__get_limit_and_offset(page)
            return user.favorites[offset: offset + limit]
        return user.favorites

    def add_movie_to_favorites(self, user_id: int, movie_id: int) -> None:
        user = self.get_by_id(user_id)
        movie = self._db_session.query(Movie).get_or_404(movie_id)

        user.favorites.append(movie)
        self._db_session.commit()

    def remote_movie_from_favorites(self, user_id: int, movie_id: int) -> None:
        user = self.get_by_id(user_id)
        movie = self._db_session.query(Movie).get_or_404(movie_id)

        with suppress(ValueError):
            user.favorites.remove(movie)
            self._db_session.commit()
