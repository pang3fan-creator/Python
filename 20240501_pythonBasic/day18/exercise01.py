"""
打印出所有的图片  .png结尾
打印所有的文本.txt 文件的创建时间 年月日
打印出所有的练习文件的路径
听闻：st_size 能够获取文件大小
使用内置高阶函数+容器函数 输出包含.png图片的大小的列表
[100,45456,452155]
"""

from pathlib import Path
from datetime import datetime

for item in Path.cwd().parent.rglob("*.png"):
    print(item)

for item in Path.cwd().parent.rglob("*.txt"):
    # 先获取创建时间  --》 时间戳转换  --》 格式化
    # item.stat().st_ctime
    # datetime.fromtimestamp(item.stat().st_ctime)
    print(datetime.fromtimestamp(item.stat().st_ctime)
          .strftime("%Y年%m月%d日 %H时%M分%S秒"))

for item in Path.cwd().parent.rglob("exercise*"):
    print(item)


print(list(map(lambda item: item.stat().st_size,
               Path.cwd().parent.rglob("*.png")
               )
           )
      )
