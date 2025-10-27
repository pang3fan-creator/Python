"""
疫情信息管理系统V1
   使用的容器嵌套完成对数据的增删改查
疫情信息管理系统V2
   使用函数重构
疫情信息管理系统V3
    使用类和对象代替字典表达疫情
疫情信息管理系统V4
    使用MVC架构 重构疫情信息管理系统

      M层  Model       模型  封装数据
      V层  View        视图  输入输出  显示菜单、选择菜单、录入信息
      C层  Controller  控制  存储/计算  疫情列表， 添加信息动作
"""


# 模型层  封装数据
class EpidemicModel:
    def __init__(self, name, new=0, now=0):
        self.name = name
        self.new = new
        self.now = now

    def display(self):
        print(f"{self.name}地区新增{self.new}人，现有{self.now}人")


# 视图层 输入输出
class EpidemicView:
    def __init__(self):
        self.controller = EpidemicController()

    # 显示菜单
    def display_menu(self):
        print("按1键添加疫情信息")
        print("按2键显示疫情信息")
        print("按3键删除疫情信息")
        print("按4键修改疫情信息")
        print("按5键退出系统")

    # 选择菜单
    def select_menu(self):
        number = input("请输入数字：")

        if number == "1":
            # 添加信息
            print("添加信息方法触发")
            self.input_epidemic()
        elif number == "2":
            # 显示信息
            print("显示信息方法触发")
            self.display_epidemic()
        elif number == "3":
            # 删除信息
            print("删除信息方法触发")
            self.delete_epidemic()
        elif number == "4":
            # 修改信息
            print("修改信息方法触发")
            self.update_epidemic()

    # 修改信息
    def update_epidemic(self):
        while True:
            model = EpidemicModel(
                name=input("请输入需要地区名称："),
                new=int(input("请输入新增人数：")),
                now=int(input("请输入现有人数：")),
            )

            if self.controller.modify_epidemic(model):
                print("修改成功")
                break
            else:
                print("修改失败")

    # 删除信息
    def delete_epidemic(self):
        while True:
            name = input("请输入要删除的地区名称：")

            # 这里最终判断的是是否删除成功
            # 如果删除成功说明地区存在， 否则就是地区不存在
            if self.controller.remove_epidemic(name):
                print("信息删除成功")
                break
            else:
                print("地区不存在")

    # 新增信息
    def input_epidemic(self):
        # 这里需要借助model类来创建数据(触发构造函数)
        # 实例化类 把得到对象给到 epidemic 变量
        epidemic = EpidemicModel(
            input("请输入地区名称："),
            int(input("请输入新增人数：")),
            int(input("请输入现有人数："))
        )
        # 在此场景的是业务逻辑中，我们需要将产生的信息加入到列表中
        # v层和m层没有创建列表的操作手段， 只有c层中有
        # 调用C层的方法给这个方法传值
        self.controller.add_epidemic(epidemic)

    # 显示信息
    def display_epidemic(self):
        # 如果想成功调用这个方法，M层拥有这个 display()就可以
        for item in self.controller.list_epidemic:
            print(vars(item))
            item.__display()


# 控制器层
class EpidemicController:
    def __init__(self):
        self.list_epidemic = []

    def modify_epidemic(self, model):
        for item in self.list_epidemic:
            if item.name == model.name:
                item.new = model.new
                item.now = model.now
                return True
        return False

    def remove_epidemic(self, name):
        # 根据地区名称来删除相关数据,删除成功返回true，反之返回false
        # 输入的name名称 和 列表中的对象的name值一致
        for i in range(len(self.list_epidemic)):
            # 如果第i个索引的元素（对象）的name值和输入的name值一致
            if self.list_epidemic[i].name == name:
                del self.list_epidemic[i]
                return True
        return False

    def add_epidemic(self, new):
        self.list_epidemic.append(new)


view = EpidemicView()

while True:
    # 显示菜单和选择菜单方法是EpidemicView类的方法
    # ==> 对象.方法
    # ==> 需要对象
    # ==> 实例化类
    # ==> 实例化 EpidemicView 类
    view.display_menu()
    view.select_menu()
