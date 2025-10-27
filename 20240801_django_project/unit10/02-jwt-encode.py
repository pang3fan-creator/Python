import jwt
import time

payload = {
    'id': 1,
    'username': 'Rose',
    'exp': int(time.time()) + 20
}
string = jwt.encode(payload=payload, key='123456')
print(string)
