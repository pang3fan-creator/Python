from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Article
from .models import AuthorBasicInfo, AuthorDetailInfo, AuthorLevel

from knowbase.utils import md5, login_required

from django.shortcuts import redirect
from django.http import HttpResponseRedirect


@login_required
def index(request):
    return render(request, 'backend/index.html')


def login(request):

    if request.method == 'GET':
        return render(request, 'backend/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        author = AuthorBasicInfo.objects.filter(username=username, password=md5(password))
        if author:
            # 将当前登录作者的相关信息存入到SESSION,后便后续在相关的视图中校验用户是否登录
            request.session['backend'] = {
                'id': author.first().pk,
                'username': author.first().username,
                'nickname': author.first().nickname,
                'face': author.first().face
            }

            returnurl = request.GET.get('returnurl', '/backend/')
            return redirect(returnurl)
        else:
            return redirect('/backend/login/')


def logout(request):
    request.session.delete('backend')

    return redirect('/backend/login/')


@login_required
def author(request):
    author = AuthorBasicInfo.objects.all()
    ###################################################
    # first_author = author.first() # AuthorBasicInfo object (5)
    # print(first_author.authordetailinfo) # AuthorDetailInfo object (5)
    # print(dir(first_author.authordetailinfo))
    ###################################################
    context = {
        'author': author
    }
    return render(request, 'backend/author-list.html', context)


@login_required
def create_author(request):
    return render(request, 'backend/author-create.html')


@login_required
def post_author(request):
    username = request.POST.get('username')

    if AuthorBasicInfo.objects.filter(username=username).exists():
        content = '''
            <script>
            history.go(-1);            
            </script>
        '''
        return HttpResponse(content, content_type='text/html')

    # 获取第一个用户等级(第一个用户等级的ID并非一定为1)
    level = AuthorLevel.objects.first()

    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    nickname = request.POST.get('nickname')
    author = AuthorBasicInfo.objects.create(
        username=username,
        password=password,
        nickname=nickname,
        # 通过模型实例的关系字段进行赋值
        level=level
    )
    ############################################

    realname = request.POST.get('realname')
    gender = request.POST.get('gender')
    birthday = request.POST.get('birthday')
    address = request.POST.get('address')

    AuthorDetailInfo.objects.create(
        realname=realname,
        gender=gender,
        birthday=birthday,
        address=address,
        # 通过数据表的外键字段进行赋值
        author_id=author.pk
    )
    return redirect('/backend/author/')


@login_required
def get_author(request, id):
    return render(request, 'backend/author-update.html')


@login_required
def put_author(request, id):
    return HttpResponse('author modified')


@login_required
def delete_author(request, id):
    return HttpResponse('author deleted')


@login_required
def category(request):
    category = Category.objects.all()
    context = {
        'category': category
    }
    return render(request, 'backend/category-list.html', context)


@login_required
def create_category(request):
    return render(request, 'backend/category-create.html')


@login_required
def post_category(request):
    catename = request.POST.get('catename')
    sort_order = request.POST.get('sort_order')
    Category.objects.create(
        catename=catename,
        sort_order=sort_order
    )
    return redirect('/backend/category/')


@login_required
def get_category(request, id):
    category = Category.objects.get(pk=id)
    context = {
        'category': category
    }
    return render(request, 'backend/category-update.html', context)


@login_required
def put_category(request, id):
    catename = request.POST.get('catename')
    sort_order = request.POST.get('sort_order')
    Category.objects.filter(pk=id).update(
        catename=catename,
        sort_order=sort_order
    )
    return HttpResponse('category modified')


@login_required
def delete_category(reuqest, id):
    return HttpResponse('category deleted')


@login_required
def article(request):
    from .models import Article

    article = Article.objects.filter(is_deleted=False)
    context = {
        'article': article
    }
    return render(request, 'backend/article-list.html', context)


@login_required
def create_article(request):
    return render(request, 'backend/article-create.html')


@login_required
def post_article(request):
    subject = request.POST.get('subject')
    category_id = request.POST.get('category_id')
    textarea = request.POST.get('textarea')
    Article.objects.create(
        subject=subject,
        content=textarea,
        category_id=category_id,
        # 应该是登录作者的ID,后续要调整
        author_id=4
    )
    return redirect('/backend/article/')


@login_required
def get_article(request, id):
    article = Article.objects.get(pk=id)
    context = {
        'article': article
    }
    return render(request, 'backend/article-update.html', context)


@login_required
def put_article(request, id):
    subject = request.POST.get('subject')
    category_id = request.POST.get('category_id')
    textarea = request.POST.get('textarea')

    Article.objects.filter(pk=id).update(
        subject=subject,
        category_id=category_id,
        content=textarea
    )

    return HttpResponse('article modified')


@login_required
def delete_article(request, id):
    Article.objects.filter(pk=id).update(is_deleted=True)
    return redirect('/backend/article/')


@login_required
def recycle_article(request):
    article = Article.objects.filter(is_deleted=True)
    context = {
        'article': article
    }
    return render(request, 'backend/recycle-list.html', context)


@login_required
def restore_article(request, id):
    article = Article.objects.filter(pk=id).update(is_deleted=False)
    return redirect('/backend/article/')


@login_required
def remove_article(request, id):
    Article.objects.filter(pk=id).delete()
    return redirect('/backend/article/')
