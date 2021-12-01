from project.dao import BaseDAO
from project.models import Genre


class GenreDAO(BaseDAO):
    __model__ = Genre
