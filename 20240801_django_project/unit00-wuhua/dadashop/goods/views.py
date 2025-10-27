import json

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.conf import settings
from .models import Catalog, SKU, SaleAttrValue
from django.db.models import F


def index(request):
    catalogs_list = []
    catalogs = Catalog.objects.all()
    for catalog in catalogs:
        catalog_dict = {
            'catalog_id': catalog.pk,
            'catalog_name': catalog.name
        }
        # 立即得到当前这个分类下的三件正常上架的商品
        sku_list = list(
            SKU.objects.values('name', 'caption', 'price', skuid=F('id'), image=F('default_image_url')).filter(
                spu__in=catalog.spu_set.all(), is_launched=True)[:3])
        # 并且添加到分类字典中，键名为sku
        catalog_dict.update({
            'sku': sku_list
        })
        catalogs_list.append(catalog_dict)
    context = {
        'code': 200,
        'base_url': settings.DADASHOP_MEDIA_URL,
        'data': catalogs_list
    }
    return JsonResponse(context)


def catalogs(request, catalog_id):
    catalog = Catalog.objects.get(pk=catalog_id)
    sku_queryset = SKU.objects.values('name', 'price', skuid=F('id'), image=F('default_image_url')).filter(
        spu__in=catalog.spu_set.all(), is_launched=True)
    ##################################################
    from django.core.paginator import Paginator
    pagesize = 1
    paginator = Paginator(sku_queryset, pagesize)
    page = paginator.get_page(request.GET.get('page', 1))
    ##################################################
    context = {
        'code': 200,
        'base_url': settings.DADASHOP_MEDIA_URL,
        'paginator': {
            'pagesize': pagesize,
            'total': sku_queryset.j()
        },
        'data': list(page)
    }
    return JsonResponse(context)


def detail(request, id):
    # 获取商品模型对象
    sku_object = SKU.objects.get(pk=id)
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # SPU的属性名称和属性ID(正向关系和反向关系同时存在) --通过values_lists()方法只指定一个字段并且结果集对元组进行了展平操作
    sku_sale_attr_id = list(sku_object.spu.spusaleattr_set.values_list('id', flat=True))
    sku_sale_attr_names = list(sku_object.spu.spusaleattr_set.values_list('name', flat=True))
    # print(sku_sale_attr_id)
    # ******************************
    bb = SaleAttrValue.objects.filter(spu_sale_attr__in=sku_sale_attr_id)
    # print(bb)
    sku_all_sale_attr_vals_id = {a: [item.pk for item in bb if a == item.spu_sale_attr_id] for a in sku_sale_attr_id}
    sku_all_sale_attr_vals_name = {a: [item.name for item in bb if a == item.spu_sale_attr_id] for a in
                                   sku_sale_attr_id}
    # print(sku_all_sale_attr_vals_id)
    # print(sku_all_sale_attr_vals_name)
    # ******************************
    '''
    # SPU的属性名称和属性ID(正向关系和反向关系同时存在) -- 通过列表推导式实现
    spusaleattr_queryset = sku_object.spu.spusaleattr_set.all()
    sku_sale_attr_id = [item.pk for item in spusaleattr_queryset]
    sku_sale_attr_names = [item.name for item in spusaleattr_queryset]
    '''
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    # SPU的属性值与ID
    sku_sale_attr_val_id = SaleAttrValue.objects.filter(spu_sale_attr__in=sku_sale_attr_id).values_list('id', flat=True)
    sku_sale_attr_val_names = SaleAttrValue.objects.filter(spu_sale_attr__in=sku_sale_attr_id).values_list('name',
                                                                                                           flat=True)
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    context = {
        "code": 200,
        "data": {
            #############################################
            # 类别信息(两次正向关系)
            "catalog_id": sku_object.spu.catalog.pk,
            "catalog_name": sku_object.spu.catalog.name,
            ################################################
            # 商品信息
            "name": sku_object.name,
            "caption": sku_object.caption,
            "price": sku_object.price,
            # 模型中的ImageFieldFile继承自 ImageFile,而ImageFile继承自File
            "image": sku_object.default_image_url.name,
            # 正向关系
            "spu": sku_object.spu.pk,
            ################################################
            #  商品信息--详情图片
            "detail_image": "v2-1.jpg",

            ################################################
            # SPU的属性名称和属性ID
            "sku_sale_attr_id": sku_sale_attr_id,
            "sku_sale_attr_names": sku_sale_attr_names,
            ################################################

            # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
            # 销售属性值
            "sku_sale_attr_val_id": list(sku_sale_attr_val_id),
            "sku_sale_attr_val_names": list(sku_sale_attr_val_names),
            # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

            # 销售属性和销售属性值的对应关系
            "sku_all_sale_attr_vals_id": sku_all_sale_attr_vals_id,
            "sku_all_sale_attr_vals_name": sku_all_sale_attr_vals_name,

            # 类6和类7：规格属性名和规格属性值
            "spec": {
                "批次": "2000",
                "数量": "2000",
                "年份": "2000"
            }
        },
        "base_url": settings.DADASHOP_MEDIA_URL
    }
    return JsonResponse(context)


def sku(request):
    from .models import SPU
    data = json.loads(request.body)
    # {'1':'1','2':'4','spuid':'1'}
    # 其中1,2代表属性名称ID,1,4代表属性值ID
    # 型号ID
    spuid = data.get('spuid')
    spu_object = SPU.objects.get(pk=spuid)
    # 获取当前型号下所有的商品集合
    sku_objects = spu_object.sku_set.all()
    # 删除spuid键 -- 因为只能通过遍历SPU的属性值来确认唯一商品，另外，SPU可能存在多个属性
    data.pop('spuid')
    # 遍历SPU的属性值
    for key,value in data.items():
        sku_objects = sku_objects.filter(sale_attr_value=value)

    if sku_objects:
        context = {
            'code':200,
            'data':sku_objects.first().pk
        }
    else:
        context ={
            'code':20001,
            'error':'对不起，指定商品不存在'
        }
    return JsonResponse(context)
