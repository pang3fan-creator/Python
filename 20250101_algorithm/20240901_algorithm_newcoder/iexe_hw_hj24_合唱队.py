# N 位同学站成一排，音乐老师要请最少的同学出列，使得剩下的 K 位同学排成合唱队形。
# 你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。
# 注意：不允许改变队列元素的先后顺序 且 不要求最高同学左右人数必须相等

# 动态规划（我是看代码随想录了解的，讲得很清楚）
def get_arr_up(arr: list):
    dp_arr = [1] * length
    for i in range(1, length):
        for j in range(i):
            if arr[i] > arr[j]:
                dp_arr[i] = max(dp_arr[j] + 1, dp_arr[i])
    return dp_arr


# 奇妙的办法（个人理解）
# 这里的意思是：
# 1.若是arr[i]是arr_tem里面最大的，就加进去，通过长度（只是长度）得到dp_arr，意思是，最长子序列长度+1
# 2.若不是，则替换arr_tem里面第一个比arr[i]大的数，并得到其位置，
# 意义是，比如最后一个数a_old被a_new替换了，那么代表着 目前为止的最长子序列的最后一个数不需要比a_old大，只需要比a_new大，便能得到相同长度的子序列
# 以此类推，倒数第二个数b_old被b_new替换了，则代表着 倒数第二、一个数需要依次比a_new,b_new大，便能得到相同长度的子序列
# 这样子不断降低大小以此更新子序列
def inc_max(arr: list):
    dp_arr = [1] * length  # 初始化dp，最小递增子序列长度为1
    arr_tem = [arr[0]]  # 创建数组
    for i in range(1, length):  # 从原序列第二个元素开始遍历
        if arr[i] > arr_tem[-1]:
            arr_tem.append(arr[i])
            dp_arr[i] = len(arr_tem)
        else:
            # 这里我没有用二分法，直接循环了
            pos = 0
            for j in range(len(arr_tem)):
                if arr[i] <= arr_tem[j]:
                    arr_tem[j] = arr[i]
                    break
    return dp_arr


# 动态规划
length = int(input())
arr = list(map(int, input().split()))

# 动态规划（我试过了，大概率会超时，小概率不会哈哈哈哈哈哈哈）
# dp_up = get_arr_up(arr)
# dp_down = get_arr_up(arr[::-1])[::-1]

# 奇妙的办法
dp_up = inc_max(arr)
dp_down = inc_max(arr[::-1])[::-1]

dp = [length - ((dp_up[i] + dp_down[i]) - 1) for i in range(length)]

print(min(dp))
