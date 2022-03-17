# from typing import Any, Dict
#
# from project.dao import GenreDAO, UserDAO
# from project.exceptions import GenreNotFoundException
# from project.services import BaseService
# from project.services.schemas import UserSchema
#
#
# class UpdateProfileInfoService(BaseService):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.user_dao = UserDAO(self._db_session)
#         self.genre_dao = GenreDAO(self._db_session)
#         self.schema = UserSchema()
#
#     def execute(
#         self,
#         user_id: int,
#         name: str = None,
#         surname: str = None,
#         favourite_genre: int = None,
#     ) -> Dict[str, Any]:
#         if favourite_genre:
#             if not self.genre_dao.get_by_id(favourite_genre):
#                 raise GenreNotFoundException
#
#         return self.schema.dump(
#             self.user_dao.update_user_info(
#                 user_id=user_id,
#                 name=name,
#                 surname=surname,
#                 favourite_genre=favourite_genre,
#             )
#         )
