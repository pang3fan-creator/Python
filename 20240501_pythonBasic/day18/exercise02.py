"""
1.创建一个目录aid2405 在这个目录下 创建一个my.txt
2.修改aid2405下的my.txt为 you.txt
3.删除aid2405目录

"""
from pathlib import Path

# 增
# Path("aid2405").mkdir()
# Path("aid2405/my.txt").touch()

# 改
Path("aid2405/my.txt").rename("aid2405/you.txt")

# 删
# Path("aid2405/my.txt").unlink()
# Path("aid2405").rmdir()
