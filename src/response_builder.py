import json

from datetime import datetime
from commonfns import timeit

def _set_key(d, k, v):
    """set dict key if its value is not None"""
    if v is not None:
        d[k] = v
    return d

def for_OK():
    """for OK response"""
    response = {}
    response = _set_key(response, 'message', 'OK')
    return json.dumps(response)

def for_ping(data):
    """for ping response"""
    response = {}
    response = _set_key(response, 'message', datetime.strftime(data.dt, '%Y-%m-%d %H:%M:%S'))
    return json.dumps(response)

