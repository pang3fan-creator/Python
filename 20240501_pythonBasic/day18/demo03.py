"""
文件管理 当前路径Day18
"""
from pathlib import Path

# 判断文件存不存在 相对路径
print(Path("haha.txt").exists())
# 天王老子来了也是false，因为python区分大小写
# 很遗憾 在我这里是true 2024年06月21日11:31:53
# windows共享文件的问题  乌班图真机无问题
print(Path("homework/hoMewOrk01.py").exists())
print(Path("../Day17/demo01.py").exists())

# 从根路径返回
print(Path.cwd())
a=Path.cwd()
print(type(a))
print(a)
print(Path.cwd().joinpath('demo01.py'))
print(Path.cwd().joinpath('demo01.py').exists())
