"""
请实现一个计票统计系统。你会收到很多投票，其中有合法的也有不合法的，请统计每个候选人得票的数量以及不合法的票数。
（注：不合法的投票指的是投票的名字不存在n个候选人的名字中！！）

"""

while True:
    try:
        n = int(input())
        names = input().strip().split(' ')
        m = int(input())
        votes = input().strip().split(' ')

        dict_names = {'Invalid': 0}
        for name in names: dict_names.setdefault(name, 0)

        for vote in votes:
            if vote in names:
                dict_names[vote] += 1
            else:
                dict_names['Invalid'] += 1

        for name in names: print(f"{name} : {dict_names[name]}")
        print(f"Invalid : {dict_names['Invalid']}")
    except:
        break
