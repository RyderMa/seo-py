from contextlib import contextmanager
from httpx import QueryParams
from sqlalchemy.orm import sessionmaker
import urllib.parse


def get_resp(message='', code=0, data=None):
    code = 0 if not message else -1
    message = message or 'success'
    res = {'code': code, 'message': message}
    if data:
        res['data'] = data
    return res


@contextmanager
def connection(DBSession: sessionmaker, autocommit=False):
    session = DBSession()
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        if autocommit:
            session.commit()
        print("------------------Connection closed------------------")
        session.close()
