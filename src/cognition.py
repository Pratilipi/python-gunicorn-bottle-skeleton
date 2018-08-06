from exceptions import *
from dbutil import *
from model import *

def health():
    result = {"state": "healthy"}
    return result

def ping_db(kwargs):
    """ping db"""
    try:
        conn = connectdb()
        cursor = conn.cursor()
        sql = """SELECT CURRENT_TIMESTAMP() as dt"""
        cursor.execute(sql)
        record_set = cursor.fetchone()
    except Exception as err:
        raise DbSelectError(err)
    finally:
        disconnectdb(conn)
    obj = PingDB()
    for name in record_set:
        setattr(obj, name, record_set[name])
    return obj

