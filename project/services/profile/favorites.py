# from typing import Any, Dict, List, Optional
#
# from project.dao import MovieDAO, UserDAO
# from project.exceptions import MovieNotFoundException
# from project.services import BaseService
# from project.services.schemas import MovieSchema
#
#
# class FavoritesService(BaseService):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.user_dao = UserDAO(self._db_session)
#         self.movie_dao = MovieDAO(self._db_session)
#         self.schema = MovieSchema(many=True)
#
#     def _check_exists(self, movie_id: int) -> None:
#         if not self.movie_dao.get_by_id(movie_id):
#             raise MovieNotFoundException
#
#     def add(self, user_id: int, movie_id: int) -> None:
#         self._check_exists(movie_id)
#         self.user_dao.add_movie_to_favorites(user_id, movie_id)
#
#     def delete(self, user_id: int, movie_id: int):
#         self._check_exists(movie_id)
#         self.user_dao.remote_from_favorites(user_id, movie_id)
#
#     def get_all(self, user_id: int, page: Optional[int] = None) -> List[Dict[str, Any]]:
#         return self.schema.dump(self.user_dao.get_favorites(user_id, page))
