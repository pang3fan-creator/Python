from django.shortcuts import render, redirect
from backend.models import Article
from .models import Comment
from django.http import HttpResponse


def index(request, id=None):
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
    return render(request, 'frontend/forget.html')


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
