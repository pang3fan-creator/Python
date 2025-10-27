"""
文件管理
"""
from pathlib import Path
from datetime import datetime

p = Path('demo01.py')
# 文件名
print(p.name)
# 是否是文件
print(p.is_file())
# 返回一个时间戳 创建时间
print(p.stat().st_ctime)

# 将时间戳转化为datetime
print(datetime.fromtimestamp(p.stat().st_ctime))
