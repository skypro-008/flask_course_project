from typing import Optional

from sqlalchemy.exc import IntegrityError

from project.dao.base import BaseDAO
from project.errors import ConflictError
from project.models import User


class UserDAO(BaseDAO[User]):
    """
    TODO: Стремная какая-то херня, надо поправить бы юзера
    """
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

    # def add_movie_to_favorites(self, user_id: int, movie_id: int) -> None:
    #     # TODO: Чет херня какая-то
    #     user = User.query.get(user_id)
    #     movie = Movie.query.get(movie_id)
    #
    #     user.favorites.append(movie)
    #     self._db_session.commit()
    #
    # def remote_from_favorites(self, user_id: int, movie_id: int) -> None:
    #     # TODO: Чет херня какая-то
    #     user = User.query.get(user_id)
    #     movie = Movie.query.get(movie_id)
    #
    #     with suppress(ValueError):
    #         user.favorites.remove(movie)
    #         self._db_session.commit()
    #
    # def get_favorites(self, user_id: int, page: Optional[int] = None) -> List[Movie]:
    #     if not (user := self._db_session.query(User).filter(User.id == user_id).one_or_none()):
    #         return []
    #
    #     if page:
    #         limit, offset = self._get_limit_and_offset(page)
    #         return user.favorites[offset: offset + limit]
    #     return user.favorites
    #
