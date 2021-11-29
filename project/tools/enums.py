from enum import Enum


class UserRole(Enum):
    employer = 'работодатель'
    applicant = 'соискатель'

    @classmethod
    def values(cls):
        _map: dict = getattr(cls, '_value2member_map_')
        return tuple(_map.keys())
