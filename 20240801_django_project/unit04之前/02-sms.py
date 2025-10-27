from ronglian_sms_sdk import SmsSDK
import random
import json

SMS_ACCOUNT_ID = '2c94811c9035ff9f019121f3f9c5326f'
SMS_ACCOUNT_TOKEN = 'f09c664202f84b2384c42deb051a0d8d'
SMS_APP_ID = '2c94811c9035ff9f019121f3fb433276'

# 构造函数的参数有：主账号ID(Account ID)，主账号令牌(Account Token)，应用ID(App ID)
sms_sdk = SmsSDK(SMS_ACCOUNT_ID, SMS_ACCOUNT_TOKEN, SMS_APP_ID)

# 发送手机短信:
# tid为模板ID
# mobile指接收短信的手机号码,多个号码之间以英文逗号分隔
# datas指要发送的短信内容，必须为元组

rand_data = random.randint(1000, 9999)

minutes = 10

res = sms_sdk.sendMessage(tid='1', mobile='18833815986', datas=(rand_data, minutes))

dict = json.loads(res)

if dict.get('statusCode') == '000000':
    print('短信发送成功')
else:
    print(dict.get('statusMsg'))
