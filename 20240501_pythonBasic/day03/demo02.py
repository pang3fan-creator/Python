"""
在终端中输入课程阶段，显示课程名称
效果：
1   python核心编程
2   python高级技术
3   web全栈
4   人工智能
"""
level = int(input("请输入课程阶段："))

if level == 1: print("python核心编程")
if level == 2: print("python高级技术")
if level == 3: print("web全栈")
if level == 4: print("人工智能")

if level == 1:
    print("python核心编程")
elif level == 2:
    print("python高级技术")
elif level == 3:
    print("web全栈")
elif level == 4:
    print("人工智能")
else:
    print("阶段错误，请重新输入")
