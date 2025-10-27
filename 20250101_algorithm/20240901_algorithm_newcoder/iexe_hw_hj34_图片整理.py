"""
一行，一个字符串，字符串中的每个字符表示一张Lily使用的图片。
Lily的所有图片按照从小到大的顺序输出
"""
while True:
    try:
        line = input().strip()
        str_1 = ''
        for i in sorted(line, key=lambda x: ord(x)): str_1 = str_1 + i
        print(str_1)
    except:
        break
