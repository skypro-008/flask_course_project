from project.dao import BaseDAO
from project.models import Movie


class MovieDAO(BaseDAO):
    __model__ = Movie
