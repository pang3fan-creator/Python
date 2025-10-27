from goods.models import SaleAttrValue, SPUSaleAttr, SPU, SKU, Brand, Catalog


# http://127.0.0.1:8000/v1/goods/1
def mysql():
    # 插入类别记录、品牌记录
    catalog_object = Catalog.objects.create(name='洗面奶')
    brand_object = Brand.objects.create(
        name='至本', logo='brand/zhiben.png', first_letter='Z')

    spu_object = SPU.objects.create(
        name='至本舒颜修护', brand_id=2, catalog_id=2)
    spusaleattr_object = SPUSaleAttr.objects.create(
        name='型号', spu=spu_object)

    # 导入型号的属性值模型
    saleattrvalue_object1 = SaleAttrValue.objects.create(
        name='新版24年6代', spu_sale_attr=spusaleattr_object)

    # 导入商品的模型
    SKU.objects.create(
        name='至本舒颜修护洁面乳—新版10年1代',
        caption='至本', price=68, cost_price=58, market_price=98,
        default_image_url='sku/zhiben-1.jpg', spu_id=4)

    # 分别获取出了前期通过Django Shell添加的商品
    # sku18 = SKU.objects.filter(pk=18)
    # sku19 = SKU.objects.get(pk=19)

    # 依次获取这4个商品的每个属性值
    # saleattrvalue7 = SaleAttrValue.objects.get(pk=7)
    # saleattrvalue8 = SaleAttrValue.objects.get(pk=8)
    # saleattrvalue9 = SaleAttrValue.objects.get(pk=9)

    # 将属性值与商品进行绑定
    # 通过正向关系实现
    # sku18.update(sale_attr_value=saleattrvalue9)
    # sku19.sale_attr_value.add(saleattrvalue7)
