"""
    demo06_image.py
"""
import random

import requests
from ua_pool import ua_list

html = requests.get(url="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201511%2F26%2F20151126170518_AurJw.thumb.700_0.jpeg&refer=http%3A%2F%2Fb-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1721987321&t=036616f3860d5798ade50f8871329441",
                    headers={"User-Agent": random.choice(ua_list)}).content
with open("girl.jpg", "wb") as f:
    f.write(html)

















