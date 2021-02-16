import os
from . import utils, entity
from typing import Union


class Environment(entity.Entity):
    def __init__(self, data: Union[dict, None] = None):
        if data is None:
            data = {}
        self._data = data

    def data(self) -> dict:
        return self._data

    @classmethod
    def current(cls) -> 'Environment':
        return cls({
            'environment_variables': os.environ,
            'current_instance': utils.current_instance()
        })
