import hashlib
from django.conf import settings
import jwt


def md5(string):
    md_5 = hashlib.md5()
    md_5.update(string.encode())
    return md_5.hexdigest()


def jwt_encode(payload):
    string = jwt.encode(payload=payload, key=settings.JWT_SECRET_KEY)
    return string


def jwt_decode(string):
    try:
        payload = jwt.decode(jwt=string, key=settings.JWT_SECRET_KEY, algorithms='HS256')
    except:
        return False
    return payload
