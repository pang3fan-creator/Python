import hashlib
import jwt
from django.conf import settings


def md5(string):
    md5 = hashlib.md5()
    md5.update(string.encode())
    return md5.hexdigest()


def jwt_encode(payload):
    string = jwt.encode(payload=payload, key=settings.JWT_SECRET_KEY)
    return string


def jwt_decode(string):
    # 如果JWT字符串被篡改的话，则会抛出异常
    # 也就是说如果存在异常的话，则代表没有被解析出来
    try:
        payload = jwt.decode(
            jwt=string,
            key=settings.JWT_SECRET_KEY,
            algorithms='HS256'
        )
        return payload
    except Exception as e:
        return False
