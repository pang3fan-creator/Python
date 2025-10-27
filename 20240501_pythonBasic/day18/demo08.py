"""
文件管理文件读写

写  修改文件 修改文件的内容
字符数 = 对象名.write(字符串)

"""
from pathlib import Path

with open("data.txt", "w", encoding="utf-8") as file:
    file.write("您好")
    file.write("大爷")
    # argument must be str, not int
    # 必须是字符串
    # file.write(18)

with open("data.txt", "r", encoding="utf-8") as file:
    print(file.read())
