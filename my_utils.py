from typing import *


def import_file_from_url(f_loc: str='https://raw.githubusercontent.com/johnsanterre/my_utils/master/my_utils.py') -> None:
    '''
    import_
    '''
    #snake eating itself
    import urllib2;
    tmp= urllib2.urlopen(f_loc);
    exec(tmp.read())


def csv_to_dict(f: str) -> Dict[Any, Any]:
    import csv
    reader = csv.DictReader(open(f))
    out = {}
    for row in reader:
        for column, value in row.items():
            out.setdefault(column, []).append(value)

    return out
