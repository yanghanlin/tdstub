#!/usr/bin/env python3

import sys
import json
import os
import pathlib

log_levels = os.environ['LOG_LEVELS'].split(',') if 'LOG_LEVELS' in os.environ else [
    'info',
    'warning',
    'error',
]


class ConfigError(Exception):
    def __init__(self, *args):
        super(ConfigError, self).__init__(*args)


def open_config(*args, **kwargs):
    path = pathlib.Path(os.environ.get('CONFIG_FILE', 'config.json'))
    if not path.exists():
        path.write_text(json.dumps({}), encoding='utf-8')
    return open(path, *args, **kwargs)


def log(message, level='info', **kwargs):
    if level not in log_levels:
        return
    if 'file' not in kwargs:
        kwargs['file'] = sys.stderr
    print('{}: {}: {}'.format(sys.argv[0], level, message), **kwargs)


def keys_from_path(path, base='ROOT'):
    res = path.split('.') if path else []
    if base is not None:
        res.insert(0, base)
    return res


def value_from_keys(config, keys, *, create_on_missing=False):
    current = config
    while len(keys) > 1:
        try:
            current = current[keys[1]]
        except KeyError as e:
            if create_on_missing:
                current[keys[1]] = {}
                current = current[keys[1]]
            else:
                raise ConfigError('key {} does not exist in level {}'.format(keys[1], keys[0]))
        keys.pop(0)
    return current


def get_config(path=''):
    with open_config('r', encoding='utf-8') as file:
        config = json.load(file)
    return value_from_keys(config, keys_from_path(path))


def set_config(path, value):
    with open_config('r', encoding='utf-8') as file:
        config = json.load(file)
    keys = keys_from_path(path)
    local_config = value_from_keys(config, keys[:-1], create_on_missing=True)
    local_config[keys[-1]] = value
    with open_config('w', encoding='utf-8') as file:
        json.dump(config, file)


def rm_config(path):
    with open_config('r', encoding='utf-8') as file:
        config = json.load(file)
    keys = keys_from_path(path)
    local_config = value_from_keys(config, keys[:-1])
    try:
        del local_config[keys[-1]]
    except KeyError:
        raise ConfigError('key {} does not exist in level {}'.format(keys[-1], keys[-2]))
    with open_config('w', encoding='utf-8') as file:
        json.dump(config, file)


def main():
    if len(sys.argv) < 2:
        log('missing action get/set/rm', 'error')
        sys.exit(1)
    try:
        res = {
            'get': get_config,
            'set': set_config,
            'rm': rm_config,
        }[sys.argv[1]](*sys.argv[2:])
        if res is None:
            return
        elif not isinstance(res, str):
            res = json.dumps(res, indent=2)
        print(res)
    except KeyError as e:
        log('invalid action {}'.format(sys.argv[1]), 'error')
        log('KeyError args = {}'.format(e.args), 'debug')
        sys.exit(1)
    except TypeError as e:
        log('invalid arguments {}'.format(', '.join(sys.argv[2:])), 'error')
        log('TypeError args = {}'.format(e.args), 'debug')
        sys.exit(1)
    except ConfigError as e:
        log(e.args[0], 'error')
        log('ConfigError args = {}'.format(e.args), 'debug')
        sys.exit(1)


if __name__ == '__main__':
    main()
