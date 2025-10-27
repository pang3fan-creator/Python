import jwt

payload = {
    'id':1,
    'username':'Tom'
}

key = '1234567'

jwt_string = jwt.encode(payload=payload,key=key)

print(jwt_string)


