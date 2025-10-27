"""
程序启动入口
"""
from usl import StuView
# 约定俗称（语法上或语言没这么要求，但程序员为了方便协同开发，共同创建的规则）的将main作为程序的主入口

# 如果直接运行py文件(模块) __name__ 就会返回  __main__
# 如果是被其他文件引入，则 __name__ 返回的是当前模块的文件名
# 恒等式  在这里 __name__ 总是返回  __main__
if __name__ == '__main__':
    print("wuhu~~")
    # 先显示菜单，再选择菜单，根据不同的输入执行不同的操作
    view = StuView()
    view.main()
else:
    print("yiyiyi~")
