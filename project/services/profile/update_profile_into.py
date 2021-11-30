from project.dao import GenreDAO, UserDAO
from project.exceptions import GenreNotFound
from project.schemas import UserSchema
from project.tools.service import BaseService


class UpdateProfileInfoService(BaseService):

    def execute(self, pk: int, name: str = None, surname: str = None, favourite_genre: int = None) -> dict:
        if favourite_genre:
            if not GenreDAO(self._db_session).get_genre_by_id(favourite_genre):
                raise GenreNotFound

        return UserSchema().dump(UserDAO(self._db_session).update_user_info(
            user_id=pk,
            name=name,
            surname=surname,
            favourite_genre=favourite_genre
        ))
