"""
输入一行，表示用来倒排的句子
输出句子的倒排结果
"""
while True:
    try:
        line = input().strip()
        str = ""
        for a in line:
            str = str + a if a.isupper() or a.islower() else str + ' '
        str = str.split(' ')[::-1]
        print(' '.join(str))
    except:
        break
