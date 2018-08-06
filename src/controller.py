import bottle
import cognition
import response_builder
import inspect

from bottle import response, hook
from commonfns import request_parser, log
from exceptions import *
from validator import *
from pprint import pprint as p

@hook('after_request')
def set_content_type():
    """set response content type"""
    response.set_header('Content-Type', 'application/json; charset=utf-8')
    response.set_header('Powered-By', 'Bottle 0.12.13')

def health():
    """health check"""
    return bottle.HTTPResponse(status=200, body=cognition.health())

@request_parser
def pingdb(**kwargs):
    """ping db"""
    try:
        data = cognition.ping_db(kwargs)
        response = response_builder.for_ping(data)
        return bottle.HTTPResponse(status=200, body=response)
    except Exception as err:
        log(inspect.stack()[0][3], "ERROR", str(err), kwargs)
        return bottle.HTTPResponse(status=500, body={"message": str(err)})
