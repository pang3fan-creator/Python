from ronglian_sms_sdk import SmsSDK
from random import randint
import json

SMS_ACCOUNT_ID = '2c94811c9035ff9f019121f3f9c5326f'
SMS_ACCOUNT_TOKEN = 'f09c664202f84b2384c42deb051a0d8d'
SMS_APP_ID = '2c94811c9035ff9f019121f3fb433276'

rand_num = randint(1000, 9999)
sms_sdk = SmsSDK(SMS_ACCOUNT_ID, SMS_ACCOUNT_TOKEN, SMS_APP_ID)
res = sms_sdk.sendMessage(tid='1', mobile='18833815986', datas=(5629,))
print(json.loads(res))

