import os
from . import utils, entity
from typing import Union
import platform
import django
import rest_framework
import socket
import ifaddr


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
            'instance': utils.current_instance(),
            'host': {
                'platform': _current_platform(),
                'runtime': _current_runtime(),
                'network': _current_network(),
                'environment_variables': os.environ,
            },
        })


def _current_platform() -> dict:
    return {
        'architecture': platform.machine(),
        'os': platform.platform(),
        'processor': platform.processor(),
    }


def _current_runtime() -> dict:
    return {
        'python': {
            'implementation': platform.python_implementation(),
            'version': platform.python_version(),
        },
        'django': django.__version__,
        'drf': rest_framework.__version__,
    }


def _current_network() -> dict:
    interfaces = {}
    for adapter in ifaddr.get_adapters():
        entry = {}
        if adapter.name != adapter.nice_name:
            entry['name'] = adapter.nice_name
        entry['ips'] = [str(ip.ip) for ip in adapter.ips]
        interfaces[adapter.name.decode()] = entry
    return {
        'hostname': socket.gethostname(),
        'interfaces': interfaces,
    }
