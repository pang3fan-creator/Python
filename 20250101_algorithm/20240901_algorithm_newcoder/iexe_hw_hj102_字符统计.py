"""
输入描述：
一个只包含小写英文字母和数字的字符串。

输出描述：
一个字符串，为不同字母出现次数的降序表示。若出现次数相同，则按ASCII码的升序输出。
"""
while True:
    try:
        s = input()
        d = {}
        for i in s:
            d.setdefault(i, 0)
            d[i] += 1
        f = sorted(d.items(), key=lambda x: (-x[1], x[0]))
        for i in f: print(i[0], end='')
    except:
        break
