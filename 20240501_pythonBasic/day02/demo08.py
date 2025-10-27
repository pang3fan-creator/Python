"""
短路求值
逻辑运算and 和 or 中，
当前一个表达式的结果能够确定整个表达式结果的时候，
后面的表达式不会被执行
代码的艺术：
把一些复杂的条件写在第一位，越复杂的条件越难满足
"""
# 此代码仅作为教学解释使用

# 逻辑与的短路求值
# true and 被执行
1 == 1 and print("Hello1")

# false and 不被执行
1 == 0 and print("Hello2")

# true  and true     true
# true  and false    false
# false and 不被执行  fasle

# 逻辑或的短路求值
# false or 被执行
1 != 1 or print("Hello3")

# true or 不被执行
1 == 1 or print("Hello4")

# true or 不被执行  true
# false or false  false
# false or true  true
