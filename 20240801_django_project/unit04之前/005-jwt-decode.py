import jwt

jwt_string = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJUb20ifQ.zNlcm7WdHleu_-GHs0y7V9u4D4yZlGuM2FHuHCe7iXU'

payload = jwt.decode(jwt=jwt_string, key='1234567', algorithms='HS256')

print(payload)
