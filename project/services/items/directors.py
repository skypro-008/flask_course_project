from project.dao.director import DirectorDAO
from project.services import ItemServiceBase
from project.exceptions import DirectorNotFoundException
from project.services.schemas import DirectorSchema


class DirectorsService(ItemServiceBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dao = DirectorDAO(self._db_session)
        self.schema = DirectorSchema
        self.not_found_exception = DirectorNotFoundException
