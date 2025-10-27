"""
输入两个字符串。第一个为短字符串，第二个为长字符串。两个字符串均由小写字母组成
如果短字符串的所有字符均在长字符串中出现过，则输出字符串"true"。否则输出字符串"false"。
"""
while True:
    try:
        s1 = input()
        s2 = input()
        for i in s1:
            if i not in s2:
                print("false")
                break
        else:
            print("true")
    except:
        break
