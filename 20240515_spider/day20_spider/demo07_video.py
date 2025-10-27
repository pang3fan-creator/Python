"""
    demo07_video.py
    1.在帖子中提取视频链接[lxml+xpath];
    2.向视频链接发请求,保存视频;
"""
import random
import requests
from lxml import etree
from ua_pool import ua_list

# 1.提取视频链接
t_url = "https://tieba.baidu.com/p/9064117740"
headers = {"User-Agent": random.choice(ua_list)}
t_html = requests.get(url=t_url, headers=headers).content.decode("utf-8", "ignore")

eobj = etree.HTML(t_html)
src_list = eobj.xpath('//embed/@data-video')
video_url = src_list[0]

# 2.抓取视频
v_html = requests.get(url=video_url, headers=headers).content
with open("girl.mp4", "wb") as f:
    f.write(v_html)










