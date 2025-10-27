"""
设计一个哈希类型的数据，用于存储用户的购物车信息，

这个信息中包括:购买的商品的ID，数量，价格及状态(是否被选定)

因为HASH中的field一定是唯一的，而商品的ID也是唯一，所以商品ID来充当field可以保证唯一性

但是像商品的数量、价格及状态等只能是HASH中的value了,在HASH中value的类型只能为数字或字符串

所以目前value只能采用字符串类型，而这个字符串类型需要将三个信息相对独立,理论上来说可以采用特定的分隔符对其进行分隔，如 数量,价格,状态或 数量#价格#状态，如果是这种方式的话确实可行，

但是在进行对数理、价格及状态进行修改时变得比较繁琐 -- 字符串拆分成列表，修改，再拼接成字符串写入

最为简单的操作时将价格、数量及状态存储成JSON格式的字典字符串  --- '{"number":1,"price":200,"status":true}'

当需要进行修改时，只需要 json.loads(字典字符串) ,此时变成了PYTHON中的字典，然后进行操作，当修改

完成后需要再完写入Redis时只需要 json.dumps(字典),此时变成了 字符串

"""
import json

from redis import Redis

redis_conn = Redis(
    host='127.0.0.1',
    port=6379,
    password=None,
    db=2,
    decode_responses=True
)

# 当前这个页面我们先通过HSET手动设置一个key,把它想像成购物车中已存在的商品
# ，购物车的一些操作，如更新特定商品的数量，状态等，在后续的PYTHON文件中实现

# tarena1代表的时后续业务中当前登录用户的用户名


redis_conn.hset('buyer_tarena1', mapping={
    # 5,6,9是当前商品的ID,在HASH中也就是field
    5: '{"number" : 3,"price" : 1249.50,"status" : true}',
    6: '{"number" : 1,"price" : 888.88,"status" : false}',
    9: '{"number" : 6,"price" : 200,"status" : true}',
})

# 读取购物车的商品信息，输入的格式如下：
# 商品ID:xxx,购买数量:xxx,单价:xxx,状态:xxx

products = redis_conn.hgetall('buyer_tarena1')
for key, json_string in products.items():
    product_item = json.loads(json_string)
    print('商品ID', key, ',购买数量:', product_item.get('number'), ',单价:', product_item.get('price'), ',状态:',
          product_item.get('status'), ',总价:', product_item.get('number') * product_item.get('price'))
