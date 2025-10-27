"""
根据命题写出代码
年龄大于18岁 并且 男生
职位是高管 或者 年薪大于5000
"""
age = (int(input("年龄：")) > 18)
sex = (input("性别：") == "男")
print(age and sex)

leader = (input("职位：") == "高管")
money = (float(input("年薪：")) > 5000)
print(leader or money)

# 优先级
# 1  ()           小括号
# 2  **           幂运算
# 3  * / // %     乘除法
# 4  + -          加减法
# 5  > < ==       比较运算
# 6  and or not   逻辑运算

# ------------------------------------------------

1 == 1 and print("1")

1 == 0 and print("2")

1 != 1 or print("3")

1 == 1 or print("4")
