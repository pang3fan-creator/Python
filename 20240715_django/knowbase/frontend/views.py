from django.shortcuts import render, redirect
from backend.models import Article
from .models import Comment
from django.http import HttpResponse
from django.conf import settings


def index(request, id=None):
    ########################

    # from django_redis import get_redis_connection
    #
    # redis_conn = get_redis_connection(alias='default')
    #
    # redis_conn.set("abcdef","123456")



    # from django.core.cache import caches
    #
    # from django.core.cache import cache
    #
    # # 测试操作Django_redis缓存
    # # cache == caches['default']
    #
    # caches['default'].add("redis_cache", "123456")
    #
    # print(caches['default'].get('redis_cache'))
    #
    # print(cache.get('redis_cache'))
    #
    # caches['default'].set('user_info_name', 'Tom')
    # caches['default'].set('user_info_password', '123456')
    # caches['default'].set('user_info_age',22)
    #
    # print('get_many:', caches['default'].get_many(['user_info_name', 'user_info_password', 'user_info_age']))
    #
    # caches['default'].incr('user_info_age', 5)
    #
    # print('age+5:', caches['default'].get('user_info_age'))
    #
    # caches['default'].decr('user_info_age', 2)
    #
    # print('age-2', caches['default'].get('user_info_age'))
    #
    # caches['default'].delete('user_info_password')
    #
    # print('password value is', caches['default'].get('user_info_password'))
    #
    #
    # caches['default'].set('users',[1,2,3,4,5,6,7])

    ########################
    # 读取所有正常的文章 -- QuerySet
    '''
    if id is None:
        article = Article.objects.filter(is_deleted=False)
    else:
        # 按模型中的(属性)字段名称进行查找
        # article = Article.objects.filter(is_deleted=False,category=id)
        # 按形成的数据表的字段名称进行查找
        article = Article.objects.filter(is_deleted=False, category_id=id)
    '''
    article = Article.objects.filter(is_deleted=False)
    if id:
        article = article.filter(category_id=id)

    #######################################################
    from django.core.paginator import Paginator
    pagesize = 2
    paginator = Paginator(article, pagesize)
    pageno = request.GET.get('pageno')
    page = paginator.get_page(pageno)
    #######################################################
    context = {
        'article': page
    }
    return render(request, 'frontend/index.html', context)


def article(request, id):
    article = Article.objects.get(pk=id)
    context = {
        'article': article
    }
    return render(request, 'frontend/article.html', context)


def register(request):
    return render(request, 'frontend/register.html')


def login(request):
    from knowbase.utils import md5
    from .models import User
    if request.method == 'GET':
        return render(request, 'frontend/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=md5(password))
        if user:
            request.session['frontend'] = {
                'id': user.first().pk,
                'username': user.first().username,
                'nickname': user.first().nickname,
                'face': user.first().face
            }
            return redirect('/')
        else:
            return redirect('/login/')


def logout(request):
    request.session.delete('frontend')
    request.session.flush()
    return redirect('/')


def comment(request, id):
    comment = Comment.objects.filter(article=id)
    context = {
        'comment': comment
    }
    return render(request, 'frontend/comment.html', context)


def forget(request):
    if request.method == 'GET':
        return render(request, 'frontend/forget.html')
    if request.method == 'POST':
        from django.core.mail import send_mail
        from django.template.loader import render_to_string
        import random
        from .models import User

        email = request.POST.get('email')

        # 查看邮件地址是否存在
        user_exists = User.objects.filter(email=email).exists()
        if not user_exists:
            return HttpResponse('Email Address dot not exists')

        verify_code = random.randint(1000, 9999)

        context = {
            'verify_code': verify_code
        }

        # 读取模板内容并与变量混合后的字符串
        html = render_to_string('email/forget.html', context)

        ###############################################

        # 使用Redis缓存存储生成的验证码 -- 方法1:直接使用Redis模块实现
        #
        # from redis import Redis
        #
        # redis_conn = Redis(
        #     host='127.0.0.1',
        #     port=6379,
        #     password=None,
        #     db=0,
        #     decode_responses=True
        # )

        #使用Redis缓存存储生成的验证码 - - 方法2: 使用django_redis模块实现

        from django_redis import get_redis_connection

        redis_conn = get_redis_connection(alias='default')

        redis_conn.set(email, verify_code, ex=300)

        ###############################################

        send_mail(
            subject='找回密码',
            message='',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            html_message=html
        )

        from knowbase.utils import md5

        key = md5(email + settings.PASSWORD_SALT)

        return redirect('/verify/?email=' + email + '&key=' + key)


def profile(request):
    if request.method == 'GET':
        return render(request, 'frontend/profile.html')
    if request.method == 'POST':
        # 获取上传文件对象
        uploaded_file = request.FILES.get('myfile')
        from django.core.files.storage import default_storage
        if uploaded_file:
            import uuid
            # 获取上传文件的名称
            filename = uploaded_file.name
            # 获取文件的扩展名
            extension = filename[filename.rfind('.') + 1:].lower()
            # 通过UUID来生成唯一的主文件名
            mainname = str(uuid.uuid1())
            # 将主文件名和扩展名拼接成新的文件名
            filenewname = f'{mainname}.{extension}'
            # 将文件上传到服务器
            default_storage.save('frontend/avatar/' + filenewname, uploaded_file)
            print('ok')

        else:
            print("no select file")
        return HttpResponse("updated")


def verify(request):
    if request.method == 'GET':
        return render(request, 'frontend/verify.html')

    if request.method == 'POST':
        # 获取用户输入的验证码
        verify = request.POST.get('verify')
        # 获取已经存储在Redis中的验证码
        # from redis import Redis
        # redis_conn = Redis(
        #     host='127.0.0.1',
        #     port=6379,
        #     password=None,
        #     db=0,
        #     decode_responses=True
        # )
        from django_redis import get_redis_connection

        redis_conn = get_redis_connection(alias='default')

        email = request.GET.get('email')

        key = request.GET.get('key')

        from knowbase.utils import md5

        verify_key = md5(email + settings.PASSWORD_SALT)

        # if key != verify_key:
        #     return HttpResponse('数据被篡改')

        verify2 = redis_conn.get(email)

        print(verify2)
        print(type(verify2))

        # 进行校验

        if verify == verify2:
            print('OK')
        else:
            print('Error')

        return HttpResponse('verified')
