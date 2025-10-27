'''
现在假设有如果结构的字符串，同时假设有两张数据表 category和products，其中

category数据表的结构如下：

id用于存储分类ID， catename用于存储分类名称

products数据表的结构如下:

id用于存储商品ID

product_name用于存储商品名称

product_caption用于存储商品标题

product_price用于存储商品价格

product_image用于存储商品的图片

category_id用于存储商品所属的分类，外键(参照category数据表的ID字段)

请把下列数据按目前的结构形成标准的SQL语句即可，如

INSERT category(id,catename) VALUES(1,'手提包');

INSERT product(id,product_name,product_caption,product_price,product_image,category_id) VALUES(1,'安踏A蓝色小尺寸','蓝色小尺寸',88.00,'sku/1_CWVre0U.png',1);

...

...



'''
context = {
    "code": 200,
    "base_url": "http://127.0.0.1:8000/media/",
    "data": [
        {"catalog_id": 1,
         "catalog_name": "手提包",
         "sku": [
             {"name": "安踏A蓝色小尺寸", "caption": "蓝色小尺寸",
              "price": "88.00", "skuid": 1, "image": "sku/1_CWVre0U.png"},
             {"name": "安踏A灰色大尺寸", "caption": "灰色大尺寸",
              "price": "139.00", "skuid": 2, "image": "sku/2_viqhhBm.png"},
             {"name": "安踏B蓝色小尺寸", "caption": "蓝色小尺寸",
              "price": "167.00", "skuid": 3, "image": "sku/3_1Dc1Us9.png"}]},
        {"catalog_id": 2,
         "catalog_name": "女士香水",
         "sku": [
             {"name": "卡罗琳娜埃莱拉（Carolina Herrera） 香水七夕情人节礼物 香柠檬之花中性淡香水 EDT 100ml",
              "caption": "卡罗琳娜埃莱拉", "price": "100.00", "skuid": 4, "image": "sku/199cf20f2541ab14.png"},
             {"name": "卡罗琳娜埃莱拉（Carolina Herrera） 香水七夕情人节礼物 CH好女孩女士香水 EDP 150ml",
              "caption": "卡罗琳娜埃莱拉", "price": "100.00", "skuid": 5, "image": "sku/41a8802e46484f77.jpg"},
             {"name": "卡罗琳娜埃莱拉（Carolina Herrera） 香水七夕情人节礼物 CH花语女士淡香水 EDT 100ml",
              "caption": "卡罗琳娜埃莱拉", "price": "100.00", "skuid": 6, "image": "sku/41a8802e46484f77.jpg"}]}
    ]}

import json

# data_list = json.loads(context).get('data')

#
# for item in data_list:
#     category_sql = f"INSERT category(id,catename) VALUES({item.get('catalog_id')},'{item.get('catalog_name')}');"
#     print(category_sql)
#     for sku_object in item.get('sku'):
#         product_sql = f"INSERT product(id,product_name,product_caption,product_price,product_image,category_id) VALUES({sku_object.get('skuid')},'{sku_object.get('name')}','{sku_object.get('caption')}',{sku_object.get('price')},'{sku_object.get('image')}',{item.get('catalog_id')});"
#         print(product_sql)
#


data_list = json.loads(context).get('data')

text = ''''
from goods.models import Category
from goods.models import Product 
'''
for item in data_list:
    text += f'''    
    a = Category.objects.create(
        catename='{item.get('catalog_name')}'
    )
    '''
    print(text)
