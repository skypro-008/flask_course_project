from project.dao import BaseDAO
from project.models import Director


class DirectorDAO(BaseDAO):
    __model__ = Director
