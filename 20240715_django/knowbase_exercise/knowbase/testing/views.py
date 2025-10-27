from django.shortcuts import render
from .models import Book
from django.db.models import F,Q
from django.db.models import Count,Avg,Sum,Max,Min
from django.core.paginator import Paginator
from backend.models import AuthorDetailInfo

# Create your views here.
def index(request):

    # 获取地址栏中的页码参数
    pageno = request.GET.get('pageno')

    # 获取全部记录
    books = Book.objects.all()

    # 实例化Paginator对象
    pagesize = 8
    paginator = Paginator(books,pagesize)

   #获取指定页码的Page对象(不仅包含分页的数据还包括有分页的其他信息，如上一页或下一页的页码等)

    page = paginator.get_page(pageno)

    # print(type(page))

    context = {
        'title': 'Django Model',
        'books': page
    }

    return render(request, 'testing/index.html', context)


def detail(request, id):
    try:
        book = Book.objects.get(id=id)
    except Exception as e:
        book = False
    context = {
        'title': '图书详情',
        'book':book
    }
    return render(request, 'testing/detail.html', context)


def field(request):
    field_by_values = Book.objects.values('id','bookname','sale_price')[:5]
    field_by_values_list = Book.objects.values_list('id', 'bookname', 'sale_price')[:5]
    field_by_only = Book.objects.only('id', 'bookname', 'sale_price')[:5]
    #为字段赋予别名

    field_by_alias = Book.objects.values('id',name=F('bookname'),price=F('sale_price'))[:5]



    context = {
        'title': '限制字段',
        'field_by_values':field_by_values,
        'field_by_values_list':field_by_values_list,
        'field_by_only':field_by_only,
        'field_by_alias':field_by_alias
    }
    return render(request, 'testing/field.html', context)


def filter(request):
    #查找第一条记录
    first_object = Book.objects.first()

    #查找最后一条记录
    last_object = Book.objects.last()

    # 查找记录是否存在
    book_object_exists = Book.objects.filter(pk=6000).exists()

    #查找id号等于 36 的图书
    # filter_by_exact = Book.objects.filter(id__exact=36)
    # filter_by_exact = Book.objects.filter(id = 36)
    # filter_by_exact = Book.objects.filter(pk = 36)
    filter_by_exact = Book.objects.filter(pk__exact = 36)

    #查找id号小于 15 的图书
    # filter_by_lt = Book.objects.filter(id__lt=15)
    filter_by_lt = Book.objects.filter(pk__lt = 15)

    #查找价格大于 500 的图书

    filter_by_gt = Book.objects.filter(sale_price__gt=500)

    #查找id号为10，20，30 的图书
    # filter_by_in = Book.objects.filter(id__in=[10, 20, 30])
    filter_by_in = Book.objects.filter(pk__in=[10,20,30])

    #查找id号介于 40 ~ 50 之间的图书
    # filter_by_range = Book.objects.filter(id__range=(40, 50))
    filter_by_range = Book.objects.filter(pk__range=(40, 50))

    #查找书名包含 明朝 的图书
    filter_by_contains = Book.objects.filter(bookname__contains='明朝')

    #查找书名以 中国 开头的图书
    filter_by_startswith = Book.objects.filter(bookname__startswith='中国')

    # 查找书名以 中国 开头且价格超过200(含)的图书

    filter_by_multiple = Book.objects.filter(bookname__startswith='中国',sale_price__gte=200)

    #查找书名以 中国 结尾的图书
    filter_by_endswith = Book.objects.filter(bookname__endswith='中国')

    #查找 销售价格超过成本价格200元 的图书

    filter_by_f = Book.objects.values('id','bookname','sale_price','cost_price',profit=F('sale_price')-F('cost_price')).filter(profit__gte=200)

    #  查找 (图书名称以中国结尾) 或者 (分类为经典著作且价格超过200) 图书
    filter_by_q = Book.objects.filter(Q(bookname__endswith='中国') | (Q(category='经典著作') & Q(sale_price__gte=200)))


    # 查找 ID为100的整倍数 的图书
    filter_by_devide = Book.objects.values('id','bookname','sale_price','publishing','category',a=F('id') % 100).filter(a=0)

    # 查找 分类不是中国史、史家名著、地方史志、历史研究与评论、书法和心理学 的图书
    filter_by_exclude = Book.objects.exclude(category__in=['中国史', '史家名著', '地方史志', '历史研究与评论', '书法', '心理学'])

    context = {
        'title': '过滤条件',
        'first_object':first_object,
        'last_object':last_object,
        'book_object_exists':book_object_exists,
        'filter_by_exact':filter_by_exact,
        'filter_by_lt':filter_by_lt,
        'filter_by_gt': filter_by_gt,
        'filter_by_in': filter_by_in,
        'filter_by_range': filter_by_range,
        'filter_by_contains': filter_by_contains,
        'filter_by_startswith': filter_by_startswith,
        'filter_by_multiple':filter_by_multiple,
        'filter_by_endswith': filter_by_endswith,
        'filter_by_f':filter_by_f,
        'filter_by_devide':filter_by_devide,
        'filter_by_exclude':filter_by_exclude,
        'filter_by_q':filter_by_q

    }

    return render(request, 'testing/filter.html', context)


def order(request):

    # 查找价格大于1000的图书，同时按价格降序排列,价格相同的话，则以ID降序排序
    books = Book.objects.filter(sale_price__gte=1000).order_by('-sale_price','-id')
    context = {
        'title': '结果排序',
        'books': books
    }
    return render(request, 'testing/order.html', context)


def aggregate(request):
    #统计所有图书的总数量
    count_all = Book.objects.j()

    #统计价格介于50~120之间的图书的总数量
    count_by_sale_price = Book.objects.filter(sale_price__range=(50,120)).j()

    #统计价格的相关信息
    aggregate_price = Book.objects.aggregate(max_price=Max('sale_price'),min_price=Min('sale_price'),avg_price=Avg('sale_price'))

    #统计出版社与出版量的统计信息
    annotate_by_publishing = Book.objects.values('publishing').annotate(pcount = Count('publishing')).order_by('-pcount').filter(pcount__gte=20)

    # 统计图书类型与出版量、价格等的统计信息
    annotate_by_category = Book.objects.values('category').annotate(ccount=Count('category'),max_price=Max('sale_price'),min_price=Min('sale_price'),avg_price=Avg('sale_price'))

    context = {
        'title': '聚合函数',
        'count_all':count_all,
        'count_by_sale_price':count_by_sale_price,
        'aggregate_price':aggregate_price,
        'annotate_by_publishing':annotate_by_publishing,
        'annotate_by_category':annotate_by_category
    }
    return render(request, 'testing/aggregate.html', context)


def onetoone(request):
    # 获取出所有用户的详细信息(有详细信息一定在基本信息，但反之则不然)
    authordetailinfo = AuthorDetailInfo.objects.all()
    context = {
        'title': '一对一关系',
        'authordetailinfo':authordetailinfo
    }
    return render(request, 'testing/onetoone.html', context)


def onetomany(request):
    context = {
        'title': '一对多关系'
    }
    return render(request, 'testing/onetomany.html', context)


def manytomany(request):
    context = {
        'title': '多对多关系'
    }
    return render(request, 'testing/manytomany.html', context)


def related(request):
    context = {
        'title': 'related_name&amp;related_query_name'
    }
    return render(request, 'testing/related.html', context)
