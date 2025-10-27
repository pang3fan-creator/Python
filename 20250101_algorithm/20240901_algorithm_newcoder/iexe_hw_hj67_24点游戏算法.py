"""
实现功能，输入任意一个数组numbers，给一个目标数target_num
判断数组中的数经过四个运算符以及加括号运算能否运算出目标数
这个问题主要使用递归和穷举法
1.	首先生成四个数的全排列
2.	然后将每个排列都穷举运算
3.	将所有可能的计算并检查是否和目标值相等
4.	处理异常，除数为零时的做法，
5.	运算精度，截断误差的影响，最后与目标数比较时应该给一个小误差阈值。
以上第2步中涉及加括号运算问题，加括号的运算可以如下处理
考虑加括号的运算可以理解为将一列数中的任意两个相邻数取出运算，然后将结果放入原位置，并递归这一过程。这种递归式的分割方法是解决包含括号运算问题的典型思路。
以上包含了括号中多个运算数的情况，因为括号中多运算数时按照运算规则从前往后计算，以上方法包含从前往后加括号计算。
定义一个四个有序数的运算函数，任意相邻位置取出两个进行加减乘除运算，运算后放入原位置，进行递归，最终得到四个有序数在加括号且四个运算符下的所有可能的运算结果。
再对四个数生成的全排列全部进行有序数的运算，与目标值比较。
"""

import itertools  # 用于生成全排列

# 允许的运算符
operators = ['+', '-', '*', '/']


# 使用递归计算结果
def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return None  # 避免除零
        return a / b


# 递归计算所有可能的结果
def evaluate(numbers):
    # 如果只有一个数字，返回它
    if len(numbers) == 1:
        return [numbers[0]]

    results = []
    # 遍历所有可能的二元操作
    for i in range(1, len(numbers)):
        left_nums = numbers[:i]
        right_nums = numbers[i:]

        left_results = evaluate(left_nums)
        right_results = evaluate(right_nums)

        # 遍历所有运算符并计算结果
        for left_result in left_results:
            for right_result in right_results:
                for op in operators:
                    result = calculate(left_result, right_result, op)
                    if result is not None:
                        results.append(result)

    return results


# 检查是否可以运算出 target_num
def can_make_target(numbers, target_num):
    # 生成数字的所有排列
    permutations = itertools.permutations(numbers)

    # 遍历所有排列并计算结果
    for perm in permutations:
        results = evaluate(list(perm))
        for result in results:
            # 考虑浮点精度，浮点数运算的截断误差问题
            if abs(result - target_num) < 1e-6:  # 使用一个小的阈值
                return True

    return False


# numbers = [4, 7, 8, 6, 100]
# target_num = 124
# result = can_make_target(numbers, target_num)
# print(f"numbers:{numbers}\nCan make {target_num}:{result}")  # 输出 True 或 False

numbers = [int(i) for i in input().split(" ")]
result = can_make_target(numbers, 24)
print(str(result).lower())  # 输出true或false
