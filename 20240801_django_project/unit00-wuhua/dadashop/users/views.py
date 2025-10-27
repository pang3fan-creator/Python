from django.http import HttpResponse
from django.http import JsonResponse
import json
from .models import UserProfile
from dadashop.utils import md5, jwt_encode, jwt_decode
from django.conf import settings


# 用户注册
def register(request):
    # 获取提交数据
    data = json.loads(request.body)
    uname = data.get('uname').strip()
    password = data.get('password').strip()
    phone = data.get('phone').strip()
    email = data.get('email').strip()
    verify = data.get('verify').strip()
    # 检测用户名是否填写
    if len(uname) == 0:
        context = {
            'code': 10001,
            'error': '用户名没有填写'
        }
        return JsonResponse(context)

    # 检测用户名的最小长度
    if len(uname) < 6:
        context = {
            'code': 10002,
            'error': '用户名长度少于6位'
        }
        return JsonResponse(context)

    # 检查用户名的最大长度
    if len(uname) > 11:
        context = {
            'code': 10003,
            'error': '用户名长度超过11位'
        }
        return JsonResponse(context)

    # 检测密码是否填写
    if len(password) == 0:
        context = {
            'code': 10006,
            'error': '密码没有填写'
        }
        return JsonResponse(context)

    # 检测密码的最小长度
    if len(password) < 6:
        context = {
            'code': 10007,
            'error': '密码长度少于6位'
        }
        return JsonResponse(context)

    # 检测密码的最小长度
    if len(password) > 12:
        context = {
            'code': 10008,
            'error': '密码长度超过12位'
        }
        return JsonResponse(context)

    # 检查邮箱的最大长度
    if len(email) > 254:
        context = {
            'code': 10010,
            'error': '邮箱格式长度超过254个字符'
        }
        return JsonResponse(context)

    # 检查手机号码是否填写
    if len(phone) == 0:
        context = {
            'code': 10012,
            'error': '手机号码没有填写'
        }
        return JsonResponse(context)

    # 检查手机号码的长度
    if len(phone) != 11:
        context = {
            'code': 10013,
            'error': '手机号码长度不合法'
        }
        return JsonResponse(context)

    # 检测验证码是否填写
    if len(verify) == 0:
        context = {
            'code': 10016,
            'error': '验证码没有填写'
        }
        return JsonResponse(context)

    # 检测验证码的长度
    if len(verify) != 4:
        context = {
            'code': 10017,
            'error': '验证码长度不足4位'
        }
        return JsonResponse(context)

    # 校验用户名的唯一性
    user_is_exists = UserProfile.objects.filter(username=uname).exists()
    if user_is_exists:
        context = {
            'code': 10001,
            'error': '用户名已经存在'
        }
        return JsonResponse(context)

    # 检测邮箱地址的唯一性
    email_is_exists = UserProfile.objects.filter(email=email).exists()
    if email_is_exists:
        context = {
            'code': 10011,
            'error': '邮箱已经被占用'
        }
        return JsonResponse(context)

    # 检测手机号码的唯一性
    phone_is_exists = UserProfile.objects.filter(phone=phone).exists()
    if phone_is_exists:
        context = {
            'code': 10015,
            'error': '手机号码已经被占用'
        }
        return JsonResponse(context)

    from django_redis import get_redis_connection

    # 校验短信验证码是否逾期
    sms_cache_key = f'sms_{phone}'
    sms_redis_conn = get_redis_connection(alias='sms')
    if not sms_redis_conn.exists(sms_cache_key):
        context = {
            'code': 10019,
            'error': '验证码逾期'
        }
        return JsonResponse(context)

    # 校验短信验证码是否正确

    sms_cache_value = sms_redis_conn.get(sms_cache_key)
    if sms_cache_value != verify:
        context = {
            'code': 10018,
            'error': '验证码错误'
        }
        return JsonResponse(context)

    # 删除手机短信验证码的缓存

    if sms_redis_conn.exists(sms_cache_key):
        sms_redis_conn.delete(sms_cache_key)

    # 产生随机数存入缓存:既充当激活的有效值，又作为激活的盐
    import random
    rand = random.randint(100000, 999999)
    code = uname + str(rand)
    # 写入缓存

    redis_conn = get_redis_connection(alias='default')
    cache_key = f'activation_{email}'
    redis_conn.set(cache_key, rand, ex=1800)

    # 发送激活邮件
    from django.template.loader import render_to_string
    html = render_to_string('activation.html', {'username': uname, 'code': md5(code)})
    from django.core.mail import send_mail
    send_mail(
        subject='达达商城::用户激活',
        message='',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        html_message=html
    )
    # 写入用户信息-- 通过模型实例的构造函数方式实现
    userprofile = UserProfile()
    userprofile.username = uname
    userprofile.password = md5(password)
    userprofile.email = email
    userprofile.phone = phone
    userprofile.save()

    #########################################

    payload = {
        'id': userprofile.pk,
        'username': uname
    }

    token = jwt_encode(payload)

    #########################################
    context = {
        'code': 200,
        'username': uname,
        'token': token,
        'carts_count': 0
    }
    return JsonResponse(context)


# 用户登录
def login(request):
    data = json.loads(request.body)
    username = data.get('username').strip()
    password = data.get('password').strip()
    carts = data.get('carts')
    # 检查用户名是否填写
    if len(username) == 0:
        context = {
            'code': 10001,
            'error': '用户名没有填写'
        }
        return JsonResponse(context)

    # 检测用户名的最小长度
    if len(username) < 6:
        context = {
            'code': 10002,
            'error': '用户名长度少于6位'
        }
        return JsonResponse(context)

    # 检测用户名的最大长度
    if len(username) > 11:
        context = {
            'code': 10003,
            'error': '用户名长度超过11位'
        }
        return JsonResponse(context)

    # 检测密码是否填写
    if len(password) == 0:
        context = {
            'code': 10006,
            'error': '密码没有填写'
        }
        return JsonResponse(context)

    # 检查密码的最小长度
    if len(password) < 6:
        context = {
            'code': 10007,
            'error': '密码长度少于6位'
        }
        return JsonResponse(context)

    # 检查密码的最大长度
    if len(password) > 12:
        context = {
            'code': 10008,
            'error': '密码长度超过12位'
        }
        return JsonResponse(context)

    # 根据用户名和密码获取用户信息
    userprofile = UserProfile.objects.filter(username=username, password=md5(password))
    if userprofile.j():
        ##############################################
        payload = {
            'id': userprofile.first().pk,
            'username': username
        }
        token = jwt_encode(payload)
        ##############################################
        context = {
            'code': 200,
            'username': username,
            'token': token,
            'carts_count': 0
        }
    else:
        context = {
            'code': 10002,
            'error': '用户名或密码错误'
        }
    return JsonResponse(context)


# 找回密码之发送邮件
def password_sms(request):
    data = json.loads(request.body)
    email = data.get('email').strip()

    # 检测邮件地址是否填写
    if len(email) == 0:
        context = {
            'code': 10040,
            'error': '邮箱地址不能为空'

        }
        return JsonResponse(context)

    # 检测邮件地址的最大长度
    if len(email) > 254:
        context = {
            'code': 10042,
            'error': '邮箱格式长度超过254个字符'

        }
        return JsonResponse(context)

    # 检测邮箱地址是否存在
    email_is_exists = UserProfile.objects.filter(email=email).exists()

    if not email_is_exists:
        context = {
            'code': 10043,
            'error': '邮箱地址不存在'

        }
        return JsonResponse(context)

    # 读取模板内容作为邮件正文
    from django.template.loader import render_to_string
    import random
    verify = random.randint(1000, 9999)
    html = render_to_string('forgot_password.html', {'verify': verify})

    # 将随机数存入Redis缓存，以备后续校验
    from django_redis import get_redis_connection
    redis_conn = get_redis_connection(alias='default')
    redis_conn.set(email, verify, ex=600)
    # 发送邮件
    from django.core.mail import send_mail
    try:
        send_mail(
            subject='达达商城::找回密码',
            message='',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            html_message=html
        )
        context = {
            'code': 200
        }
    except Exception as e:
        context = {
            'code': 20001,
            'error': '服务器内部错误导致邮件发送失败'
        }

    return JsonResponse(context)


# 找回密码之校验验证码
def password_verification(request):
    data = json.loads(request.body)
    email = data.get('email').strip()
    code = data.get('code')
    # 检测邮箱是否填写
    if len(email) == 0:
        context = {
            'code': 10050,
            'error': '邮箱地址不能为空'

        }
        return JsonResponse(context)

    # 检测邮箱的最大长度
    if len(email) > 254:
        context = {
            'code': 10051,
            'error': '邮箱格式长度超过254个字符'

        }
        return JsonResponse(context)

    # 检测验证码最小长度
    if len(code) < 4:
        context = {
            'code': 10053,
            'error': '验证码长度不足4位'

        }
        return JsonResponse(context)

    # 检测验证码最大长度
    if len(code) > 4:
        context = {
            'code': 10054,
            'error': '验证码长度超过4位'

        }
        return JsonResponse(context)

    # 检测邮箱是否存在
    email_is_exists = UserProfile.objects.filter(email=email).exists()

    if not email_is_exists:
        context = {
            'code': 10052,
            'error': '邮箱地址不存在'

        }
        return JsonResponse(context)

    # 检验cache key是否存在
    from django_redis import get_redis_connection
    redis_conn = get_redis_connection(alias='default')
    if not redis_conn.exists(email):
        context = {
            'code': '10056',
            'error': '验证码逾期'
        }
        return JsonResponse(context)

    # 检验输入的验证码是否存与cache key中的验证码一致
    if code != redis_conn.get(email):
        context = {
            'code': '10055',
            'error': '验证码错误'
        }
        return JsonResponse(context)

    if redis_conn.exists(email):
        redis_conn.delete(email)

    context = {
        'code': 200
    }
    return JsonResponse(context)


# 找回密码之更新密码
def password_new(request):
    data = json.loads(request.body)
    email = data.get('email').strip()
    password1 = data.get('password1').strip()
    password2 = data.get('password2').strip()
    # 检测邮箱是否填写
    if len(email) == 0:
        context = {
            'code': 10060,
            'error': '邮箱地址不能为空'

        }
        return JsonResponse(context)

    # 检测邮箱的最大长度
    if len(email) > 254:
        context = {
            'code': 10061,
            'error': '邮箱格式长度超过254个字符'

        }
        return JsonResponse(context)

    # 检测密码的最小长度
    if len(password1) < 6:
        context = {
            'code': 10063,
            'error': '密码长度少于6位'
        }
        return JsonResponse(context)

    # 检测密码的最大长度
    if len(password1) > 12:
        context = {
            'code': 10064,
            'error': '密码长度超过12位'
        }
        return JsonResponse(context)

    # 检测两次密码是否一致
    if password1 != password2:
        context = {
            'code': 10065,
            'error': '两次密码不一致'
        }
        return JsonResponse(context)

    # 检测邮箱地址是否存在
    email_is_exists = UserProfile.objects.filter(email=email).exists()

    if not email_is_exists:
        context = {
            'code': 10062,
            'error': '邮箱地址不存在'

        }
        return JsonResponse(context)

    # 更新用户密码
    UserProfile.objects.filter(email=email).update(password=md5(password1))
    context = {
        'code': 200
    }
    return JsonResponse(context)


# 登录情况下更改密码
def change_password(request, username):
    data = json.loads(request.body)
    oldpassword = data.get('oldpassword').strip()
    password1 = data.get('password1').strip()
    password2 = data.get('password2').strip()
    # 检测密码的最小长度
    if len(password1) < 6:
        context = {
            'code': 10071,
            'error': '旧密码长度少于6位'
        }
        return JsonResponse(context)

    # 检测密码的最大长度
    if len(password1) > 12:
        context = {
            'code': 10071,
            'error': '旧密码长度超过12位'
        }
        return JsonResponse(context)

    if len(password2) < 6:
        context = {
            'code': 10073,
            'error': '新密码长度少于6位'
        }
        return JsonResponse(context)

    # 检测密码的最大长度
    if len(password2) > 12:
        context = {
            'code': 10074,
            'error': '新密码长度超过12位'
        }
        return JsonResponse(context)

    if password1 != password2:
        context = {
            'code': 10075,
            'error': '两次密码不一致'

        }
        return JsonResponse(context)

    # 检测用户名是否存在
    userprofile = UserProfile.objects.filter(username=username)

    if not userprofile:
        context = {
            'code': 10076,
            'error': '用户名不存在'
        }
        return JsonResponse(context)

    # 必须保证路径转换器中的username为当前登录用户

    # 校验用户输入的旧密码与数据库的密码是否一致

    if md5(oldpassword) != userprofile.first().password:
        context = {
            'code': '10077',
            'error': '旧密码错误'
        }
        return JsonResponse(context)

    userprofile.update(password=md5(password1))

    context = {
        'code': 200
    }
    return JsonResponse(context)


# 用户激活
def activation(request):
    username = request.GET.get('username')
    code = request.GET.get('code')
    user_is_exists = UserProfile.objects.filter(username=username).exists()
    if not user_is_exists:
        context = {
            'code': 10021,
            'error': '指定用户不存在'
        }
        return JsonResponse(context)

    userprofile = UserProfile.objects.get(username=username)

    from django_redis import get_redis_connection

    redis_conn = get_redis_connection(alias='default')

    cache_key = f'activation_{userprofile.email}'

    if not redis_conn.exists(cache_key):
        context = {
            'code': 10022,
            'error': '激活码过期,请查收邮件后重新激活'
        }
        # 重新再发送激活邮件
        return JsonResponse(context)

    cache_value = redis_conn.get(cache_key)

    if md5(username + cache_value) != code:
        context = {
            'code': 10023,
            'error': '数据被篡改'
        }
        return JsonResponse(context)

    UserProfile.objects.filter(username=username).update(is_active=True)
    # 激活成功后删除cache key
    if redis_conn.exists(cache_key):
        redis_conn.delete(cache_key)
    context = {
        'code': 200
    }

    return JsonResponse(context)


# 发送手机短信验证码
def sms_code(request):
    data = json.loads(request.body)
    phone = data.get('phone').strip()
    # 检验手机号是否被占用
    phone_is_exists = UserProfile.objects.filter(phone=phone).exists()
    if phone_is_exists:
        context = {
            'code': 10015,
            'error': '手机号码已经被占用'
        }
        return JsonResponse(context)
    # 实例化对象
    from ronglian_sms_sdk import SmsSDK
    import random
    sms_sdk = SmsSDK(settings.SMS_ACCOUNT_ID, settings.SMS_ACCOUNT_TOKEN, settings.SMS_APP_ID)

    # 产生随机数
    rand_data = random.randint(1000, 9999)

    # 短信内容的有效期
    minutes = 10

    # 将随机数存入缓存以备后续作为校验的参照
    cache_key = f'sms_{phone}'
    from django_redis import get_redis_connection
    redis_conn = get_redis_connection(alias='sms')
    redis_conn.set(cache_key, rand_data, ex=minutes * 60)

    # 发送手机短信
    res = sms_sdk.sendMessage(tid='1', mobile=phone, datas=(rand_data, minutes))

    # 解析响应
    dict = json.loads(res)

    if dict.get('statusCode') == '000000':
        context = {
            'code': 200
        }
    else:
        context = {
            'code': dict.get('statusCode'),
            'error': dict.get('statusMsg')
        }
    return JsonResponse(context)


# 地址管理类
from django.views import View


class AddressView(View):

    # 新增地址
    def post(self, request, username):
        # 从请求头获取JWT字符串
        authorization = request.headers.get('Authorization')

        # 解析JWT字符串，以获取payload
        payload = jwt_decode(authorization)

        # 如果JWT没有被正确解析
        if not payload:
            context = {
                'code': 10112,
                'error': '用户登录数据被篡改'
            }
            return JsonResponse(context)

        ###############################
        # 获取数据
        data = json.loads(request.body)
        receiver = data.get('receiver')
        address = data.get('address')
        receiver_phone = data.get('receiver_phone')
        postcode = data.get('postcode')
        tag = data.get('tag')
        # 数据校验
        if len(receiver) == 0:
            context = {
                'code': 10101,
                'error': '收货人姓名为空'
            }
            return JsonResponse(context)

        if len(receiver) > 10:
            context = {
                'code': 10102,
                'error': '收货人姓名长度超过10个字符'
            }
            return JsonResponse(context)

        if len(address) == 0:
            context = {
                'code': 10103,
                'error': '收货人详细地址为空'
            }
            return JsonResponse(context)

        if len(address) > 100:
            context = {
                'code': 10104,
                'error': '收货人详细地址长度超过100个字符'
            }
            return JsonResponse(context)
        # 验证收货人联系电话
        if len(receiver_phone) == 0:
            context = {
                'code': 10105,
                'error': '收货人联系电话为空'
            }
            return JsonResponse(context)

        if len(receiver_phone) != 11:
            context = {
                'code': 10106,
                'error': '收货人联系电话长度不合法'
            }
            return JsonResponse(context)
        # 验证邮政编码
        if len(postcode) == 0:
            context = {
                'code': 10108,
                'error': '邮政编码为空'
            }
            return JsonResponse(context)

        if len(postcode) != 6:
            context = {
                'code': 10109,
                'error': '邮政编码长度不合法'
            }
            return JsonResponse(context)
        # 验证地址标签
        if len(tag) == 0:
            context = {
                'code': 10110,
                'error': '地址标签为空'
            }
            return JsonResponse(context)

        if len(tag) > 10:
            context = {
                'code': 10111,
                'error': '地址标签长度超过10个字符'
            }
            return JsonResponse(context)

        # #########################################
        # 在登录数据没有被篡改的情况下，解析出来的数据为字典类型
        # 包括当前登录用户的id和username
        user_profile_id = payload.get('id')
        # #########################################

        # 为当前登录用户新增收货地址
        from .models import Address
        Address.objects.create(
            receiver=receiver,
            address=address,
            receiver_mobile=receiver_phone,
            postcode=postcode,
            tag=tag,
            # 如果当前用户的所有正常地址总数为0的话，则新增地址为默认地址
            is_default=not UserProfile.objects.get(pk=user_profile_id).address_set.filter(is_delete=False).j(),
            user_profile_id=user_profile_id
        )
        context = {
            'code': 200,
            'data': '收货地址添加成功'
        }
        return JsonResponse(context)

    # 查询地址
    def get(self, request, username):
        ##################################################
        # 从请求头获取JWT字符串
        authorization = request.headers.get('Authorization')

        # 解析JWT字符串，以获取payload
        payload = jwt_decode(authorization)

        # 如果JWT没有被正确解析
        if not payload:
            context = {
                'code': 10112,
                'error': '用户登录数据被篡改'
            }
            return JsonResponse(context)
        ##################################################
        from .models import Address
        user_profile = UserProfile.objects.get(username=payload.get('username'))

        # ***********************************************

        # 通过一对多的反向关系查找到当前用户的所有地址信息

        # a = user_profile.address_set.values().filter(is_delete=False)

        # 根据已解析出来的登录用户ID来查找其所有地址信息

        # b = Address.objects.values().filter(user_profile_id=payload.get('id'), is_delete=False)

        # ***********************************************

        # 前后端分离的项目中，一定要时刻注意values()方法
        addresslist = Address.objects.values('id', 'receiver', 'address', 'receiver_mobile', 'postcode', 'tag',
                                             'is_default').filter(user_profile=user_profile, is_delete=False)
        if addresslist.j():
            context = {
                'code': 200,
                'addresslist': list(addresslist)
            }
        else:
            context = {
                'code': 10120,
                'error': '暂无地址信息,请添加'
            }
        return JsonResponse(context)

    # 修改地址
    def put(self, request, username, id):
        # 从请求头获取JWT字符串
        authorization = request.headers.get('Authorization')

        # 解析JWT字符串，以获取payload
        payload = jwt_decode(authorization)

        # 如果JWT没有被正确解析
        if not payload:
            context = {
                'code': 10112,
                'error': '用户登录数据被篡改'
            }
            return JsonResponse(context)
        # 获取数据
        data = json.loads(request.body)
        receiver = data.get('receiver')
        address = data.get('address')
        receiver_mobile = data.get('receiver_mobile')
        tag = data.get('tag')
        # 数据校验
        if len(receiver) == 0:
            context = {
                'code': 10101,
                'error': '收货人姓名为空'
            }
            return JsonResponse(context)

        if len(receiver) > 10:
            context = {
                'code': 10102,
                'error': '收货人姓名长度超过10个字符'
            }
            return JsonResponse(context)

        if len(address) == 0:
            context = {
                'code': 10103,
                'error': '收货人详细地址为空'
            }
            return JsonResponse(context)

        if len(address) > 100:
            context = {
                'code': 10104,
                'error': '收货人详细地址长度超过100个字符'
            }
            return JsonResponse(context)
        # 验证收货人联系电话
        if len(receiver_mobile) == 0:
            context = {
                'code': 10105,
                'error': '收货人联系电话为空'
            }
            return JsonResponse(context)

        if len(receiver_mobile) != 11:
            context = {
                'code': 10106,
                'error': '收货人联系电话长度不合法'
            }
            return JsonResponse(context)

        # 验证地址标签
        if len(tag) == 0:
            context = {
                'code': 10110,
                'error': '地址标签为空'
            }
            return JsonResponse(context)

        if len(tag) > 10:
            context = {
                'code': 10111,
                'error': '地址标签长度超过10个字符'
            }
            return JsonResponse(context)

        #########################################
        # 验证地址是否存在
        from .models import Address
        address_is_exists = Address.objects.filter(pk=id, is_delete=False)
        if not address_is_exists:
            context = {
                'code': 10113,
                'error': '指定收货地址不存在'
            }
            return JsonResponse(context)

        #########################################
        # 验证地址是否为当前登录用户的地址

        ##########################################################
        # 获取当前用户的所有地址
        # addresslist = Address.objects.filter(user_profile_id=payload.get('id'), is_delete=False)

        # 获取当前地址(该地址并非一定为当前用户地址)
        # current_address = Address.objects.get(pk=id)

        # 用以下代码取代:当前用户是否存在当前地址

        address_is_exists = Address.objects.filter(user_profile_id=payload.get('id'), is_delete=False, pk=id).exists()

        ############################################################

        if not address_is_exists:
            context = {
                'code': 10114,
                'error': '收货地址信息与用户信息不匹配'
            }
            return JsonResponse(context)

        # 更新地址信息
        Address.objects.filter(pk=id).update(
            receiver=receiver,
            address=address,
            receiver_mobile=receiver_mobile,
            tag=tag
        )
        context = {
            'code': 200,
            'data': '收货地址编辑成功'
        }
        return JsonResponse(context)

    # 删除地址
    def delete(self, request, username, id):
        from .models import Address
        # 如果删除了默认地址，则设置为非默认地址，然后再删除
        Address.objects.filter(pk=id).update(is_default=False, is_delete=True)
        # 将当前用户的正常地址中第一个设置为默认地址
        next_sibling = UserProfile.objects.get(username=username).address_set.filter(is_default=False,
                                                                                     is_delete=False).first()
        if next_sibling:
            next_sibling.is_default = True
            next_sibling.save()

        context = {
            'code': 200,
            'data': '地址信息删除成功'
        }
        return JsonResponse(context)


# 设置默认地址
def address_default(request, username):
    data = json.loads(request.body)
    id = data.get('id')
    from .models import Address
    # 将原来的默认地址修改为非默认地址
    UserProfile.objects.get(username=username).address_set.filter(is_delete=False, is_default=True).update(
        is_default=False)
    # 将当前地址设置为默认地址
    Address.objects.filter(pk=id).update(is_default=True)
    context = {
        'code': 200,
        'data': '默认地址设置成功'
    }
    return JsonResponse(context)


# 微博授权
def weibo_authorization(request):
    context = {
        'code': 200,
        'oauth_url': f'https://api.weibo.com/oauth2/authorize?client_id={settings.WEIBO_APP_ID}&redirect_uri={settings.WEIBO_CALLBACK_URI}&response_type=code'
    }
    return JsonResponse(context)


#
class WeiBoUserView(View):
    def get(self, request):
        code = request.GET.get('code')
        # 现在要用code去微博服务器换令牌,此时向微博服务器发送请求
        import requests
        # 1.微博服务器的哪个URL发送请求及发送什么类型的请求及有哪些数据要提交
        url = 'https://api.weibo.com/oauth2/access_token'
        data = {
            'client_id': settings.WEIBO_APP_ID,
            'client_secret': settings.WEIBO_APP_SECRET_KEY,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': settings.WEIBO_CALLBACK_URI
        }
        res = requests.post(url=url, data=data)
        # 2.微博服务器返回的数据是什么
        access_token = res.json().get('access_token')
        wuid = res.json().get('uid')
        ###################################################
        # 根据现有的access_token和wuid在微博表中进行查询
        from .models import WeiboProfile
        weiboprofile_is_exists = WeiboProfile.objects.filter(access_token=access_token, wuid=wuid).exists()
        # 如果未存在相关记录, 则插入记录
        if not weiboprofile_is_exists:
            weiboprofile = WeiboProfile.objects.create(
                access_token=access_token,
                wuid=wuid
            )
            # print('你肯定是第一次扫码来，我记住你了---没有绑过')
            context = {
                'code': 201,
                'uid': weiboprofile.pk
            }
            return JsonResponse(context)
        else:
            # 如果可以查询到，再查看是否绑定过用户

            weiboprofile = WeiboProfile.objects.get(access_token=access_token, wuid=wuid)

            if weiboprofile.user_profile:
                # 如果绑定过用户的话，则返回 {'code': '200', 'username': '用户表中的用户名', 'token': jwt}
                from dadashop.utils import jwt_encode
                payload = {
                    'id': weiboprofile.user_profile.pk,
                    'username': weiboprofile.user_profile.username
                }
                context = {
                    'code': 200,
                    'username': weiboprofile.user_profile.username,
                    'token': jwt_encode(payload)
                }
                return JsonResponse(context)
            else:
                # 如果没有绑过的话, 则返回 {'code': '201', 'uid': 微博表中的记录ID}
                context = {
                    'code': 201,
                    'uid': weiboprofile.pk
                }
                return JsonResponse(context)

    def post(self, request):
        # 1.获取用户名、密码、邮箱、电话等信息，然后写入到用户表
        data = json.loads(request.body)
        uid = data.get('uid')
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        phone = data.get('phone')
        from .models import UserProfile
        from dadashop.utils import md5, jwt_encode
        user_profile = UserProfile.objects.create(
            username=username,
            password=md5(password),
            email=email,
            phone=phone
        )
        # 2.获取新插入用户的ID
        # 3.再更新微博表
        return HttpResponse("ok")


def bind_user(request):
    data = json.loads(request.body)
    uid = data.get('uid')
    username = data.get('username')
    password = data.get('password')
    from .models import UserProfile
    from dadashop.utils import md5
    # 1.获取用户名和密码并且进行查找操作 -- 用户表完成
    userprofile = UserProfile.objects.get(username=username, password=md5(password))
    # 2.找到用户之后可以获取到登录用户的ID，然后更新微博表
    from .models import WeiboProfile
    WeiboProfile.objects.filter(pk=uid).update(user_profile_id=userprofile.pk)
    from dadashop.utils import jwt_encode
    payload = {
        'id': userprofile.pk,
        'username': userprofile.username
    }
    context = {
        'code': 200,
        'username': username,
        'token': jwt_encode(payload),
        'carts_count': 0
    }
    return JsonResponse(context)
