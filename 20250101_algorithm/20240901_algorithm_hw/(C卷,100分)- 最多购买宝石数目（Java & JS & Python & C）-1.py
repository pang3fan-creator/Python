# 输入获取
n = int(input())  # 橱窗中宝石的总数量

gems = []  # n个宝石的价格
for _ in range(n):
    gems.append(int(input()))

v = int(input())  # 你拥有的钱


# 算法入口
def getResult():
    # 记录题解
    ans = 0

    # 双指针
    l = 0
    r = 0

    # 双指针范围内的和
    window_sum = 0

    while r < n:
        # 加入r指针指向的元素
        window_sum += gems[r]

        if window_sum <= v:
            # 如果总和不超过拥有的钱，则继续加入后面的
            r += 1
        else:
            # 如果总和超过了拥有的钱，则 [l, r-1] 范围的宝石是能够买下的，记录此时的宝石数量 r-1 - l + 1
            ans = max(ans, r - l)

            flag = False

            while l < r:
                # 由于纳入r位置宝石后，总和超过了拥有的钱，因此我们尝试丢弃l指针宝石，即l++
                window_sum -= gems[l]
                l += 1

                if window_sum <= v:
                    # 如果丢弃l宝石后，总和不超过拥有的钱，则继续纳入r后面的宝石
                    r += 1
                    flag = True
                    break

            if flag:
                continue

            # 如果把 l ~ r - 1 范围宝石都丢弃了，总和任然超过拥有的钱，那么就r宝石的价值就超过了手中的钱，此时双指针范围内不能包含r位置
            # 此时可以将l,r全部移动到r+1位置
            r += 1
            l = r
            window_sum = 0

    # 收尾操作
    if window_sum <= v:
        ans = max(ans, r - l)

    return ans


# 算法调用
print(getResult())
