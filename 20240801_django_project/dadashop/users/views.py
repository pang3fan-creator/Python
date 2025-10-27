import json
import random

import requests
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import View
from django_redis import get_redis_connection
from ronglian_sms_sdk import SmsSDK

from dadashop.utils import md5, jwt_encode, jwt_decode
from users.models import UserProfile, Address, WeiboProfile


def register(request):
    data = json.loads(request.body)
    verify = data['verify'].strip()
    uname = data.get('uname').strip()
    phone = data.get('phone').strip()
    email = data.get('email').strip()
    password = data.get('password').strip()

    # -----校验区-----
    if len(uname) == 0: return JsonResponse({'code': 10001, 'error': '用户名没有填写'})
    if len(uname) < 6: return JsonResponse({'code': 10002, 'error': '用户名长度少于6位'})
    if len(uname) > 11: return JsonResponse({'code': 10003, 'error': '用户名长度超过11位'})
    if len(password) == 0: return JsonResponse({'code': 10006, 'error': '密码没有填写'})
    if len(password) < 6: return JsonResponse({'code': 10007, 'error': '密码长度少于6位'})
    if len(password) > 12: return JsonResponse({'code': 10008, 'error': '密码长度超过12位'})
    if len(email) > 254: return JsonResponse({'code': 10010, 'error': '邮箱格式长度超过254个字符'})
    if len(phone) == 0: return JsonResponse({'code': 10012, 'error': '手机号码没有填写'})
    if len(phone) != 11: return JsonResponse({'code': 10013, 'error': '手机号码长度不合法'})
    if len(verify) == 0: return JsonResponse({'code': 10016, 'error': '验证码没有填写'})
    if len(verify) != 4: return JsonResponse({'code': 10017, 'error': '验证码长度不足4位'})
    # 校验用户名的唯一性
    user_is_exists = UserProfile.objects.filter(username=uname)
    if user_is_exists: return JsonResponse({'code': 10001, 'error': '用户名已经存在'})
    # 检测邮箱地址的唯一性
    email_is_exists = UserProfile.objects.filter(email=email).exists()
    if email_is_exists: return JsonResponse({'code': 10011, 'error': '邮箱已经被占用'})
    # 检测手机号码的唯一性
    phone_is_exists = UserProfile.objects.filter(phone=phone).exists()
    if phone_is_exists: return JsonResponse({'code': 10015, 'error': '手机号码已经被占用'})
    # 对手机验证码的校验
    redis_conn = get_redis_connection(alias='default')
    if verify != redis_conn.get(phone): JsonResponse({'code': 10038, 'error': '手机验证码不正确'})

    # 发送验证邮箱
    rand = str(random.randint(100000, 999999))
    code = md5(uname + rand)
    rdis_conn = get_redis_connection(alias='default')
    rdis_conn.set(email, rand, ex=1800)
    send_mail(subject='找回密码', message='', from_email=settings.EMAIL_HOST_USER,
              recipient_list=[email], html_message=render_to_string(
            'email/register.html', {'username': uname, 'code': code}))
    UserProfile.objects.create(username=uname, password=md5(password), phone=phone, email=email)

    # 确认无误，发送账号信息
    token = jwt_encode({'id': user_is_exists.first().pk, 'username': uname})
    context = {'code': 200, 'username': uname, 'token': token, 'carts_count': 0}
    return JsonResponse(context)


def login(request):
    data = json.loads(request.body)
    username = data.get('username').strip()
    password = data.get('password').strip()
    # carts = data.get('carts').strip()

    # 校验区
    if len(username) == 0: return JsonResponse({'code': 10001, 'error': '用户名没有填写'})
    if len(username) < 6: return JsonResponse({'code': 10002, 'error': '用户名长度少于6位'})
    if len(username) > 11: return JsonResponse({'code': 10003, 'error': '用户名长度超过11位'})
    if len(password) == 0: return JsonResponse({'code': 10006, 'error': '密码没有填写'})
    if len(password) < 6: return JsonResponse({'code': 10007, 'error': '密码长度少于6位'})
    if len(password) > 12: return JsonResponse({'code': 10008, 'error': '密码长度超过12位'})

    userprofile = UserProfile.objects.filter(username=username, password=md5(password))
    if not userprofile.j():
        context = {'code': 10002, 'error': '用户名或密码错误'}
    else:
        token = jwt_encode({'id': userprofile.first().pk, 'username': username})
        context = {'code': 200, 'username': username, 'token': token, 'carts_count': 0}
    return JsonResponse(context)


def sms(request):
    email = json.loads(request.body).get('email').strip()

    # 检测区
    if len(email) == 0: return JsonResponse({'code': 10040, 'error': '邮箱地址不能为空'})
    if len(email) > 254: return JsonResponse({'code': 10042, 'error': '邮箱格式长度超过254个字符'})
    email_is_exists = UserProfile.objects.filter(email=email).exists()
    if not email_is_exists: return JsonResponse({'code': 10043, 'error': '邮箱地址不存在'})

    verify_code = random.randint(1000, 9999)
    redis_conn = get_redis_connection(alias='default')
    redis_conn.set(email, verify_code, ex=600)
    try:
        send_mail(
            subject='找回密码', message='',
            from_email=settings.EMAIL_HOST_USER, recipient_list=[email],
            html_message=render_to_string('email/forget.html', {'verify_code': verify_code}))
        context = {'code': 200, 'data': '邮件发送成功'}
    except Exception as e:
        context = {'code': 20001, 'error': '服务器内部错误导致邮件发送失败'}
    return JsonResponse(context)


def verification(request):
    email = json.loads(request.body).get('email')
    code = json.loads(request.body).get('code')
    # 校验区
    if len(email) == 0: return JsonResponse({'code': 10050, 'error': '邮箱地址不能为空'})
    if len(email) > 254: return JsonResponse({'code': 10051, 'error': '邮箱格式长度超过254个字符'})
    if len(code) < 4: return JsonResponse({'code': 10053, 'error': '验证码长度不足4位'})
    if len(code) > 4: return JsonResponse({'code': 10054, 'error': '验证码长度超过4位'})
    # 检测邮箱是否存在
    email_is_exists = UserProfile.objects.filter(email=email).exists()
    if not email_is_exists: return JsonResponse({'code': 10052, 'error': '邮箱地址不存在'})

    redis_conn = get_redis_connection(alias='default')
    redis_code = redis_conn.get(email)
    if redis_code == code: context = {'code': 200, 'data': '验证码通过', 'email': email}
    if redis_code != code: context = {'code': 403, 'error': 'error reason'}
    return JsonResponse(context)


def new(request):
    email = json.loads(request.body).get('email').strip()
    password1 = json.loads(request.body).get('password1').strip()
    password2 = json.loads(request.body).get('password2').strip()

    # 校验区
    if len(email) == 0: return JsonResponse({'code': 10060, 'error': '邮箱地址不能为空'})
    if len(email) > 254: return JsonResponse({'code': 10061, 'error': '邮箱格式长度超过254个字符'})
    if len(password1) < 6: return JsonResponse({'code': 10063, 'error': '密码长度少于6位'})
    if len(password1) > 12: return JsonResponse({'code': 10064, 'error': '密码长度超过12位'})
    if password1 != password2: return JsonResponse({'code': 10065, 'error': '两次密码不一致'})

    # 检测邮箱地址是否存在
    email_is_exists = UserProfile.objects.filter(email=email).exists()
    if not email_is_exists: return JsonResponse({'code': 10062, 'error': '邮箱地址不存在'})
    UserProfile.objects.filter(email=email).update(password=md5(password1))
    return JsonResponse({'code': 200})


def password(request, username):
    data = json.loads(request.body)
    oldpassword = data.get('oldpassword').strip()
    password1 = data.get('password1').strip()
    password2 = data.get('password2').strip()

    # 校验区
    if len(password1) < 6: return JsonResponse({'code': 10007, 'error': '密码长度少于6位'})
    if len(password1) > 12: return JsonResponse({'code': 10008, 'error': '密码长度超过12位'})
    if password2 != password1: return JsonResponse({'code': 10007, 'error': '还有问题，大哥'})

    user_info = UserProfile.objects.filter(username=username, password=md5(oldpassword))
    user_info.update(password=md5(password1))
    return JsonResponse({'code': 200})


def activation(request):
    username = request.GET.get('username')
    code = request.GET.get('code')
    # 校验区
    try:
        userprofile = UserProfile.objects.get(username=username)
    except Exception as e:
        return JsonResponse({'code': 10021, 'error': '指定用户不存在'})
    redis_conn = get_redis_connection(alias='default')
    if not redis_conn.exists(userprofile.email): return JsonResponse({'code': 10022, 'error': '过期'})
    cache_value = redis_conn.get(userprofile.email)
    if md5(username + cache_value) != code: return JsonResponse({'code': 10023, 'error': '数据被篡改'})
    UserProfile.objects.filter(username=username).update(is_active=True)
    if redis_conn.exists(userprofile.email): redis_conn.delete(userprofile.email)

    return JsonResponse({'code': 200})


def sms_code(request):
    phone_number = json.loads(request.body).get('phone').strip()
    # ---------对手机号唯一性的校验-------
    user_info = UserProfile.objects.filter(phone=phone_number)
    if user_info: return JsonResponse({'code': 10015, 'error': '手机号已经存在！'})

    rand_num = random.randint(1000, 9999)
    sms_sdk = SmsSDK(settings.SMS_ACCOUNT_ID, settings.SMS_ACCOUNT_TOKEN, settings.SMS_APP_ID)
    res = json.loads(sms_sdk.sendMessage(tid='1', mobile=phone_number, datas=(rand_num, 10)))
    if res.get('statusCode') != '000000': return JsonResponse({'code': res.get('statusCode'), 'error': '发送失败'})
    redis_conn = get_redis_connection(alias='default')
    redis_conn.set(phone_number, rand_num, 600)
    return JsonResponse({'code': 200})


class AddressView(View):
    @staticmethod
    def get(request, username):
        authorization = request.headers.get('Authorization')
        payload = jwt_decode(authorization)
        user_info = UserProfile.objects.get(username=payload['username'])
        try:
            address = Address.objects.filter(user_profile=user_info, is_delete=False).values(
                'id', 'receiver', 'receiver_mobile', 'postcode', 'tag', 'address', 'is_default')
            return JsonResponse({"code": 200, "addresslist": list(address)})
        except Exception as e:
            return JsonResponse({'code': 10120, 'error': '暂无地址信息'})

    @staticmethod
    def post(request, username):

        # ----校验数据是否被篡改----
        authorization = request.headers.get('Authorization')
        payload = jwt_decode(authorization)
        if not payload: return JsonResponse({'code': 10112, 'error': '用户登录数据被篡改'})

        # ------以下：获取数据------
        data = json.loads(request.body)
        tag = data.get('tag')
        address = data.get('address')
        receiver = data.get('receiver')
        postcode = str(data.get('postcode'))
        receiver_phone = data.get('receiver_phone')

        # -----以下：校验区-----
        if not receiver: JsonResponse({'code': 10101, 'error': '收货人姓名为空'})
        if len(receiver) > 10: JsonResponse({'code': 10102, 'error': '姓名长度超过10个字符'})
        if not address: JsonResponse({'code': 10103, 'error': '收货人详细地址为空'})
        if len(address) > 100: JsonResponse({'code': 10104, 'error': '详细地址长度超过100个字符'})
        if not receiver_phone: JsonResponse({'code': 10105, 'error': '收货人电话为空'})
        if len(receiver_phone) != 11: JsonResponse({'code': 10106, 'error': '联系电话长度不合法'})
        if not postcode: JsonResponse({'code': 10108, 'error': '邮政编码为空'})
        if len(postcode) != 6: JsonResponse({'code': 10108, 'error': '邮政编码长度不合法'})

        # -----以下：校验成功，写入数据库，返回信息------
        Address.objects.all().create(
            user_profile_id=payload['id'], receiver=receiver, address=address,
            postcode=postcode, receiver_mobile=receiver_phone, tag=tag,
            is_default=not UserProfile.objects.get(pk=payload['id']).address_set.filter(
                is_delete=False).j())
        return JsonResponse({'code': 200, 'data': '收货地址添加成功'})

    @staticmethod
    def put(request, username, id):
        # 信息解析区1
        authorization = request.headers.get('Authorization')
        payload = jwt_decode(authorization)
        if not payload: return JsonResponse({'code': 10112, 'error': '用户登录数据被篡改'})

        # 信息解析区2
        user_address = json.loads(request.body)
        id = user_address['id']
        tag = user_address['tag']
        address = user_address['address']
        receiver = user_address['receiver']
        receiver_mobile = user_address['receiver_mobile']

        if not receiver: return JsonResponse({"code": 10101, "error": "收货人姓名为空"})

        # 修改区
        user = Address.objects.all().filter(id=id)
        if user:
            user.update(address=address, receiver=receiver, tag=tag, receiver_mobile=receiver_mobile)
        else:
            return JsonResponse({'code': 10113, 'error': '指定收货地址不存在'})
        return JsonResponse({"code": 200, "data": "收货地址编辑成功"})

    @staticmethod
    def delete(request, username, id):
        authorization = request.headers.get('Authorization')
        payload = jwt_decode(authorization)
        if not payload: return JsonResponse({'code': 10112, 'error': '用户登录数据被篡改'})
        try:
            Address.objects.all().filter(id=id).update(is_delete=True)
            return JsonResponse({"code": 200, "data": "地址信息删除成功"})
        except:
            return JsonResponse({"code": 10100, "error": "指定信息不存在"})


def default(request, username):
    address_id = json.loads(request.body).get('id')
    user_id = jwt_decode(request.headers.get('Authorization')).get('id')
    Address.objects.filter(user_profile_id=user_id).update(is_default=False)
    Address.objects.filter(id=address_id).update(is_default=True)
    return JsonResponse({'code': 200, 'data': "设为默认成功！"})


def weibo(request):
    path = f'https://api.weibo.com/oauth2/authorize?client_id={settings.WEIBO_APP_ID}&response_type=code&redirect_uri={settings.WEIBO_CALLBACK_URI}'
    return JsonResponse({'oauth_url': path, 'code': 200})


class WeiBoUsers(View):
    @staticmethod
    def get(request):
        code = request.GET.get('code')
        url = 'https://api.weibo.com/oauth2/access_token'
        data = {'client_id': settings.WEIBO_APP_ID, 'grant_type': "authorization_code",
                'code': code, 'redirect_uri': settings.WEIBO_CALLBACK_URI,
                'client_secret': settings.WEIBO_SECRET_KEY}
        res = requests.post(url=url, data=data)

        # {'access_token': '2.00z5DrJDkoIvXBe952152bcaa6Z14E','uid': '2894029985'}
        access_token = res.json().get('access_token')
        uid = res.json().get('uid')

        weibo_user = WeiboProfile.objects.all().filter(wuid=uid, access_token=access_token)
        if not weibo_user:
            weibo_user.create(access_token=access_token, wuid=uid)
            return JsonResponse({'code': '201', 'uid': uid})

        user_info = weibo_user.first().user_profile
        if not user_info: return JsonResponse({'code': '201', 'uid': uid})
        user_token = jwt_encode({'id': user_info.pk, 'username': user_info.username})
        context = {'code': '200', 'username': user_info.username, 'token': user_token}
        return JsonResponse(context)

    @staticmethod
    def post(self, request):
        data = json.loads(request.body)
        uid = data.get('uid')
        uname = data.get('username').strip()
        password = data.get('password').strip()
        phone = data.get('phone').strip()
        email = data.get('email').strip()

        # ----校验区----
        if len(uname) == 0: return JsonResponse({'code': 10001, 'error': '用户名没有填写'})
        if len(uname) < 6: return JsonResponse({'code': 10002, 'error': '用户名长度少于6位'})
        if len(uname) > 11: return JsonResponse({'code': 10003, 'error': '用户名长度超过11位'})
        if len(password) == 0: return JsonResponse({'code': 10006, 'error': '密码没有填写'})
        if len(password) < 6: return JsonResponse({'code': 10007, 'error': '密码长度少于6位'})
        if len(email) > 254: return JsonResponse({'code': 10010, 'error': '邮箱格式长度超过254个字符'})
        if len(phone) == 0: return JsonResponse({'code': 10012, 'error': '手机号码没有填写'})
        if len(phone) != 11: return JsonResponse({'code': 10013, 'error': '手机号码长度不合法'})
        # 校验用户名的唯一性
        user_is_exists = UserProfile.objects.filter(username=uname)
        if user_is_exists: return JsonResponse({'code': 10001, 'error': '用户名已经存在'})
        # 检测邮箱地址的唯一性
        email_is_exists = UserProfile.objects.filter(email=email).exists()
        if email_is_exists: return JsonResponse({'code': 10011, 'error': '邮箱已经被占用'})
        # 检测手机号码的唯一性
        phone_is_exists = UserProfile.objects.filter(phone=phone).exists()
        if phone_is_exists: return JsonResponse({'code': 10015, 'error': '手机号码已经被占用'})

        rand = str(random.randint(100000, 999999))
        code = md5(uname + rand)
        rdis_conn = get_redis_connection(alias='default')
        rdis_conn.set(email, rand, ex=1800)
        send_mail(
            subject='找回密码', message='',
            from_email=settings.EMAIL_HOST_USER, recipient_list=[email],
            html_message=render_to_string('email/register.html', {'username': uname, 'code': code}))
        user_info = UserProfile.objects.create(
            username=uname, password=md5(password), phone=phone, email=email)
        WeiboProfile.objects.all().filter(wuid=uid).update(user_profile=user_info)
        token = jwt_encode({'id': user_is_exists.pk, 'username': uname})
        return JsonResponse({'code': 200, 'username': uname, 'token': token, 'carts_count': 0})


def bind_user(request):
    data = json.loads(request.body)
    uid = data.get('uid')
    username = data.get('username')
    password = data.get('password')

    user_info = UserProfile.objects.all().filter(username=username, password=md5(password))
    if not user_info: return JsonResponse({'code': 10002, 'error': '用户名或密码错误'})
    WeiboProfile.objects.all().filter(wuid=uid).update(user_profile=user_info.first())
    payload = {'id': user_info.first().pk, 'username': user_info.first().username}
    context = {'code': '200', 'username': user_info.first().username, 'token': jwt_encode(payload)}
    return JsonResponse(context)
