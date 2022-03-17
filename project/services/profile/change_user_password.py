# from project.dao import UserDAO
# from project.exceptions import UpdatePasswordException
# from project.services import BaseService
# from project.utils.security import compare_passwords, generate_password_hash
#
#
# class ChangeUserPasswordService(BaseService):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.user_dao = UserDAO(self._db_session)
#
#     def execute(self, user_id: int, old_password: str, new_password: str) -> None:
#         if user := self.user_dao.get_by_id(user_id):
#             if compare_passwords(user.password, old_password):
#                 self.user_dao.update_user_password(
#                     user_id=user_id, password=generate_password_hash(new_password)
#                 )
#                 return None
#         raise UpdatePasswordException
