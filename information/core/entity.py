from typing import Union, Any, Callable


class Entity:
    def data(self) -> Union[list, tuple, dict, str, int, float, None]:
        return NotImplemented


def normalize(src: Any, *, ignore_errors=True) -> Union[list, tuple, dict, str, int, float, None, object]:
    if type(src) in (str, int, float, type(None)):
        return src
    elif type(src) in (list, tuple):
        return type(src)(map(normalize, src))
    elif type(src) == dict:
        res = {}
        for key in src:
            res[key] = normalize(src[key])
        return res
    elif isinstance(src, Entity):
        return normalize(src.data())
    elif hasattr(src, 'data') and isinstance(src.data, Callable):
        return normalize(src.data())
    elif ignore_errors:
        return src
    else:
        raise TypeError('{} cannot be normalized'.format(src))
