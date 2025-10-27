
# 导入类别模型
from goods.models import Catalog

# 插入类别记录
catalog_object = Catalog.objects.create(
	name='女士香水'
)

# 导入品牌模型
from goods.models import Brand

# 插入品牌记录

brand_object = Brand.objects.create(
	name='卡罗琳娜埃莱拉',
	logo='ka.png',
	first_letter = 'K'
)

# 导入型号(SPU)模型
from goods.models import SPU

spu_object = SPU.objects.create(
	name='中性香水',
	brand=brand_object,
	catalog=catalog_object
)


# 导入型号的属性名称模型
from goods.models import SPUSaleAttr

spusaleattr_object = SPUSaleAttr.objects.create(
	name='型号',
	spu=spu_object
)

# 导入型号的属性值模型

from goods.models import SaleAttrValue

saleattrvalue_object1 = SaleAttrValue.objects.create(
	name='香柠檬之花',
	spu_sale_attr=spusaleattr_object
)

saleattrvalue_object2 = SaleAttrValue.objects.create(
	name='CH好女孩',
	spu_sale_attr=spusaleattr_object
)

saleattrvalue_object3 = SaleAttrValue.objects.create(
	name='CH花语',
	spu_sale_attr=spusaleattr_object
)


saleattrvalue_object4 = SaleAttrValue.objects.create(
	name='香根草天堂',
	spu_sale_attr=spusaleattr_object
)


# 导入商品的模型

from goods.models import SKU

SKU.objects.create(
	name='卡罗琳娜埃莱拉（Carolina Herrera） 香水七夕情人节礼物 香柠檬之花中性淡香水 EDT 100ml',
	caption='卡罗琳娜埃莱拉', 
	price=100,
	cost_price=100,
	market_price=100,
	default_image_url='199cf20f2541ab14.png',
	spu=spu_object
)


SKU.objects.create(
	name='卡罗琳娜埃莱拉（Carolina Herrera） 香水七夕情人节礼物 CH好女孩女士香水 EDP 150ml',
	caption='卡罗琳娜埃莱拉', 
	price=100,
	cost_price=100,
	market_price=100,
	default_image_url='b1f58498027fc7a3.png',
	spu=spu_object
)



SKU.objects.create(
	name='卡罗琳娜埃莱拉（Carolina Herrera） 香水七夕情人节礼物 CH花语女士淡香水 EDT 100ml',
	caption='卡罗琳娜埃莱拉', 
	price=100,
	cost_price=100,
	market_price=100,
	default_image_url='41a8802e46484f77.jpg',
	spu=spu_object
)



SKU.objects.create(
	name='卡罗琳娜埃莱拉（Carolina Herrera） 香水七夕情人节礼物 香根草天堂中性淡香水 EDT 100ml',
	caption='卡罗琳娜埃莱拉', 
	price=100,
	cost_price=100,
	market_price=100,
	default_image_url='199cf20f2541ab14.png',
	spu=spu_object
)



     
     
     