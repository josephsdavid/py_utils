from typing import *

GenericFun = Callable[..., Any]


def import_file_from_url(
    f_loc: str = "https://raw.githubusercontent.com/josephsdavid/py_utils/master/my_utils.py",
) -> None:
    """
    import this file wherever we want
    """
    # snake eating itself
    import urllib2

    tmp = urllib2.urlopen(f_loc)
    exec(tmp.read())


def csv_to_dict(f: str) -> Dict[Any, Any]:
    import csv

    reader = csv.DictReader(open(f))
    out = {}
    for row in reader:
        for column, value in row.items():
            out.setdefault(column, []).append(value)

    return out


def curry(func: GenericFun) -> GenericFun:
    """
    curry: curry decorator for any function
    """

    def curried(*args, **kwargs):
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            return func(*args, **kwargs)
        return lambda *args2, **kwargs2: curried(
            *(args + args2), **dict(kwargs, **kwargs2)
        )

    return curried

def inverse_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
    return dict((v, k) for (k, v) in d.items())

def transpose_tuple(l: List[Tuple], t: Callable = tuple) -> Tuple:
    return t(*zip(*l))
