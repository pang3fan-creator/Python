import json

str1 = '{"statusCode":"000000","templateSMS":{"smsMessageSid":"1290f4c9fb4f46eb906638937e6ca222","dateCreated":"20240808140641"}}'
str2 = '{"statusCode":"160038","statusMsg":"短信验证码发送过频繁"}'

dict1 = json.loads(str1)
dict2 = json.loads(str2)
print(dict1.get('statusCode'))
print(dict2.get('statusCode'), dict2.get('statusMsg'))
