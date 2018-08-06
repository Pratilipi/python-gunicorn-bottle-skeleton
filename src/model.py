from datetime import datetime

LANGUAGE = ['hindi', 'marathi', 'tamil', 'telugu', 'bengali', 'kannada', 'gujarati', 'malayalam']

INT_ATTR = []
STR_ATTR = []
DT_ATTR = ['dt']

class PingDB:
    def __init__(self, kwargs=[], full=True):
        """init"""
        setattr(self, 'name', 'pingdb')
        if full:
            for name in STR_ATTR: setattr(self, name, None)
            for name in INT_ATTR: setattr(self, name, 0)
            for name in DT_ATTR: setattr(self, name, datetime.utcnow())
        for name in kwargs:
            setattr(self, name, kwargs[name])

