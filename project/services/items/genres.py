from project.dao import GenreDAO
from project.services import ItemServiceBase
from project.exceptions import GenreNotFoundException
from project.services.schemas import GenreSchema


class GenresService(ItemServiceBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dao = GenreDAO(self._db_session)
        self.schema = GenreSchema
        self.not_found_exception = GenreNotFoundException
