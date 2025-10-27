"""
获取目前目录工程内(month01)所有的.py文件代码的字符数量

"""
from pathlib import Path

toal_count = 0
for item in Path.cwd().parent.rglob("*.py"):
    print(item)
    with open(item, "r", encoding="utf-8") as file:
        toal_count += len(file.read())

print(toal_count)

list1 = ["heh", "xx"]
print(sum(len(item) for item in list1))


