import json

from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import F
from django.http import JsonResponse, HttpResponse

from goods.models import SKU, Catalog, SPU, SPUSpec, SKUImage, SPUSaleAttr, SaleAttrValue, SKUSpecValue, Brand
from .djangoshell import mysql as my_sql


def index(request):
    catalogs_list = []
    catalogs = Catalog.objects.all()
    for catalog in catalogs:
        catalog_dict = {'catalog_id': catalog.pk, 'catalog_name': catalog.name}
        # 立即得到当前这个分类下的三件正常上架的商品
        sku_list = SKU.objects.filter(spu__in=catalog.spu_set.all()).values(
            'name', 'caption', 'price', skuid=F('id'), image=F('default_image_url'))[:3]
        # 并且添加到分类字典中，键名为sku
        catalog_dict.update({'sku': [item for item in sku_list]})
        catalogs_list.append(catalog_dict)
    # print(catalogs_list)
    context = {'code': 200, "data": catalogs_list, 'base_url': settings.DADASHOP_MEDIA_URL}
    return JsonResponse(context)


def mysql(request):
    # 这个是偷懒用的链接
    my_sql()
    return HttpResponse('heihei')


def catalogs(request, id):
    page = request.GET.get('page', 1)
    launched = request.GET.get('launched')
    catalog = Catalog.objects.all().filter(pk=id).first()

    sku = SKU.objects.all().values('name', 'caption', 'price', image=F('default_image_url'))
    pagesize = 6
    paginator = Paginator(sku, pagesize)
    paginator_page = paginator.get_page(page)

    # 测试
    # print(launched, page, paginator_page)

    context = {'code': 200, "data": list(paginator_page), 'base_url': settings.DADASHOP_MEDIA_URL,
               "paginator": {"pagesize": pagesize, "total": sku.j()}}
    return JsonResponse(context)


def detail(request, id):
    sku_obj = SKU.objects.all().get(pk=id)
    spusaleattr = sku_obj.spu.spusaleattr_set.all()
    # print(sku_obj, spusaleattr)

    # 类4：销售属性
    sku_sale_attr_id = [i.pk for i in spusaleattr]
    sku_sale_attr_names = [i.name for i in spusaleattr]
    # print(sku_sale_attr_names, sku_sale_attr_id)

    # ------以下为测试区，并且已经成功了------
    # 类5：销售属性值
    # sku_sale_attr_val = SaleAttrValue.objects.all().filter(spu_sale_attr__in=spusaleattr)
    # sku_sale_attr_val_id = list(sku_sale_attr_val.values_list('id', flat=True))
    # sku_sale_attr_val_names = list(sku_sale_attr_val.values_list('name', flat=True))
    # 类5：销售属性值
    # sku_sale_attr_val_id = []
    # sku_sale_attr_val_names = []
    # for item in spusaleattr:
    #     sku_sale_attr_val_id.extend([i.pk for i in item.saleattrvalue_set.all()])
    #     sku_sale_attr_val_names.extend([i.name for i in item.saleattrvalue_set.all()])
    # 销售属性和销售属性值的对应关系
    # sku_all_sale_attr_vals_id = {item.pk: [i.pk for i in item.saleattrvalue_set.all()]
    #                              for item in spusaleattr}
    # sku_all_sale_attr_vals_name = {item.pk: [i.name for i in item.saleattrvalue_set.all()]
    #                                for item in spusaleattr}

    # 类5：销售属性值
    # 销售属性和销售属性值的对应关系
    sku_sale_attr_val_id = []
    sku_sale_attr_val_names = []
    sku_all_sale_attr_vals_id = {}
    sku_all_sale_attr_vals_name = {}
    for item in spusaleattr:
        sku_all_sale_attr_vals_id[item.pk] = [i.pk for i in item.saleattrvalue_set.all()]
        sku_sale_attr_val_id.extend(sku_all_sale_attr_vals_id[item.pk])
        sku_all_sale_attr_vals_name[item.pk] = [i.name for i in item.saleattrvalue_set.all()]
        sku_sale_attr_val_names.extend(sku_all_sale_attr_vals_name[item.pk])

    print(sku_sale_attr_val_names, sku_sale_attr_val_id)
    print(sku_all_sale_attr_vals_name, sku_all_sale_attr_vals_id)

    data_dict = {  # 类1:类别id 类别name
        "catalog_id": sku_obj.spu.catalog.pk, "catalog_name": sku_obj.spu.catalog.name,

        # 类2：SKU
        "name": sku_obj.name, "caption": sku_obj.caption, "price": sku_obj.price,
        "image": sku_obj.default_image_url.name, "spu": sku_obj.spu.pk,

        # 类3：详情图片
        "detail_image": 'sku_obj.skuimage_set.all().first().image.name',

        # 类4：销售属性
        "sku_sale_attr_id": sku_sale_attr_id, "sku_sale_attr_names": sku_sale_attr_names,

        # 类5：销售属性值
        "sku_sale_attr_val_id": sku_sale_attr_val_id, "sku_sale_attr_val_names": sku_sale_attr_val_names,

        # 销售属性和销售属性值的对应关系
        "sku_all_sale_attr_vals_id": sku_all_sale_attr_vals_id,
        "sku_all_sale_attr_vals_name": sku_all_sale_attr_vals_name,

        # 类6和类7：规格属性名和规格属性值
        "spec": {"批次": "2000", "数量": "2000", "年份": "2000"}}
    context = {"code": 200, "data": data_dict, "base_url": "http://127.0.0.1:8000/media/"}
    return JsonResponse(context)


def sku(request):
    data = json.loads(request.body)
    jwt_token = request.headers.get('Authorization')
    spuid = data.pop('spuid')
    print(data, jwt_token)

    spu_object = SPU.objects.get(pk=spuid)
    sku_objects = spu_object.sku_set.all()
    for k, v in data.items():
        sku_objects = sku_objects.filter(sale_attr_value=v)
    if sku_objects:
        context = {'code': 200, 'data': sku_objects.first().pk}
    else:
        context = {'code': 20001, 'error': '对不起，指定商品不存在'}

    return JsonResponse(context)
