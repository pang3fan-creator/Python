import jwt
import time

# # 生成token
# token = jwt.encode({'uname':'chaogege'}, '123456',algorithm='HS256')
# print(token)

# 验证签发者：issuer
token = jwt.encode({'uname':'chaogege','iss':'dadashop.com'}, '123456', algorithm='HS256')
result = jwt.decode(token, '123456', algorithms='HS256', issuer='dadashop.com')
print(result)

# 验证有效期
token = jwt.encode({'uname':'chaogege', 'exp':time.time()+10}, '123456', algorithm='HS256')
time.sleep(2)
result = jwt.decode(token, '123456', algorithms='HS256')
print(result)