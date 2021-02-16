from . import entity
from typing import Union
from rest_framework import views


class Request(entity.Entity):
    def __init__(self, data: Union[dict, None] = None):
        if data is None:
            data = {}
        self._data = data

    def data(self) -> dict:
        return self._data

    @classmethod
    def from_request(cls, request: views.Request) -> 'Request':
        return Request({
            'path': request.path,
            'method': request.method,
            'headers': request.headers,
            'query_params': request.query_params,
            'data': request.data,
        })
