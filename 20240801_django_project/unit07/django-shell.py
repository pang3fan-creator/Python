
from goods.models import SKU

from goods.models import SaleAttrValue

# # 分别获取出了前期通过Django Shell添加的商品
# sku4 = SKU.objects.get(pk=4)
# sku5 = SKU.objects.get(pk=5)
# sku6 = SKU.objects.get(pk=6)
# sku7 = SKU.objects.get(pk=7)
#
# # 依次获取这4个商品的每个属性值
#
# saleattrvalue4 = SaleAttrValue.objects.get(pk=7)
# saleattrvalue5 = SaleAttrValue.objects.get(pk=8)
# saleattrvalue6 = SaleAttrValue.objects.get(pk=9)
# saleattrvalue7 = SaleAttrValue.objects.get(pk=10)

# 将属性值与商品进行绑定
# 通过正向关系实现
sku4 = SKU.objects.get(pk=4)
saleattrvalue4 = SaleAttrValue.objects.get(pk=7)
sku4.sale_attr_value.add(saleattrvalue4)

sku5.sale_attr_value.add(saleattrvalue5)

sku6.sale_attr_value.add(saleattrvalue6)

sku7.sale_attr_value.add(saleattrvalue7)