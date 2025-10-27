import jwt

string = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJSb3NlIiwiZXhwIjoxNzIzODg2MDkxfQ.dNRO8mlbfwNFQl8VQw-7QVhVtw2oNslNpOG0_vxUSkk'
try:
    payload = jwt.decode(jwt=string, key='123456', algorithms='HS256')
    print(payload)
except jwt.ExpiredSignatureError as e:
    print('签名过期')
except jwt.InvalidSignatureError as e:
    print('Error')
