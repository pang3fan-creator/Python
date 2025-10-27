"""
文件管理 增删改
"""
from pathlib import Path
from datetime import datetime

# 增
# 文件
Path("a.txt").touch()
# 目录
# Path("test").mkdir()  # 如果存在会报错
# Path("a").mkdir(exist_ok=True)  # 如果存在不会报错

# 删
# Path("a.txt").unlink()
# Path("test").rmdir()# 如果不存在会报错
target = Path("test")
if target.exists():
    target.rmdir()

# 改
# Path('a.txt').rename('A.txt')

target1 = Path('A.txt')
# with_name 实际上并不会修改文件名而是创建了一个新对象
new_name = target1.with_name("hehe.txt")
target1.rename(new_name)
