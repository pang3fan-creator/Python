"""
文件管理
"""
from pathlib import Path
from datetime import datetime
import glob

# parent 父级
# for item in Path.cwd().parent.iterdir():

# 显示当前目录下的所有信息  文件和目录
# for item in Path.cwd().iterdir():
#     print(item)
# print(Path.cwd().iterdir())

# 通配符(1层) "*.zip" "day1*"
for item in Path.cwd().parent.glob("*/demo*"):
    print(item)

# # 递归搜索(所有层)  * 代表0个或0个以上
for item in Path.cwd().parent.rglob("*"):
    print(item)
# print(glob.glob("*"))
