"""
员工信息管理系统MVC
    定义员工模型类(实例变量：姓名、岗位、薪资)
    定义员工视图类
      定义显示菜单函数
      定义选择菜单函数
      定义录入员工函数(姓名、岗位、薪资)
      定义查看员工函数(姓名、岗位、薪资)
      定义删除员工函数(姓名)  依靠姓名删除
      定义更新员工函数(岗位、薪资)依靠姓名更新
    定义员工控制器类
      定义列表
      定义添加员工函数
      定义删除员工函数
      定义修改员工函数
"""


# 模型层
class DepModel:
    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary

    def display(self):
        print(f"{self.name}的岗位是{self.job}，薪资是{self.salary}")


# 视图层
class DepView:
    def __init__(self):
        # 私有属性
        self.__controller = DepController()

    # 公共方法
    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    # 显示菜单 私有方法
    def __display_menu(self):
        print("按1添加员工")
        print("按2显示员工")
        print("按3删除员工")
        print("按4修改员工")

    # 选择菜单
    def __select_menu(self):
        num = input("请选择：")

        if num == "1":
            self.__input_emp()
        elif num == "2":
            self.__display_emp()
        elif num == "3":
            self.__del_emp()
        elif num == "4":
            self.__update_emp()

    # 录入员工
    def __input_emp(self):
        # model = DepModel("张三", "办公室扫地僧", 100)
        model = DepModel(
            input("请输入员工姓名："),
            input("请输入员工岗位："),
            float(input("请输入员工薪资："))
        )
        # 内容放在列表中保存 ==> 存储  ==> C层
        # 对象.方法 add_emp()
        self.__controller.add_emp(model)

    # 显示员工
    def __display_emp(self):
        # self ==> v层对象
        # 有 __controller属性，它的值是对象
        # 那个对象中有employees属性，它的值是列表
        for item in self.__controller.employees:
            # 对象的属性和值组成的字典对象
            print(vars(item))
            # m层的方法
            item.__display()
            # print(item.name)

            # 字典
            # v = {
            #     # 键：值(字典)
            #     "__controller": {
            #         # 键：值(列表)
            #         "employees": [
            #             # 元素(字典)，元素，元素...
            #             {
            #                 # 键：值(字符串)
            #                 'name': '123',
            #                 'job': '12',
            #                 'salary': 123.0},
            #             {'name': '123', 'job': '12', 'salary': 123.0},
            #             {'name': '123', 'job': '12', 'salary': 123.0}
            #         ]}
            # }

            # 删除员工

    # 删除员工
    def __del_emp(self):
        name = input("请输入员工姓名：")
        # c层的删除方法
        if self.__controller.remove_emp(name):
            print("删除成功")
        else:
            print("删除失败")

    # 修改员工
    def __update_emp(self):
        name = input("请输入修改的员工姓名：")
        model = DepModel(
            input("请输入新的员工姓名："),
            input("请输入员工新岗位："),
            float(input("请输入员工薪资："))
        )

        if not self.__controller.modfiy_emp(name, model):
            print("修改失败")
        else:
            print("修改成功")


# 控制层
class DepController:

    def __init__(self):
        self.employees = []

    # 添加
    def add_emp(self, model):
        self.employees.append(model)

    # 删除
    def remove_emp(self, name):
        for item in self.employees:
            if item.name == name:
                self.employees.remove(item)
                # for i in range(len(self.employees)):
                #     if self.employees[i].name == name:
                #         del self.employees[i]
                return True
        return False

    # 修改
    def modfiy_emp(self, name, model):
        for item in self.employees:
            if item.name == name:
                # 内置属性 存储对象的属性(实例变量)的字典表示
                print(item.__dict__)
                print(vars(item))
                item.__dict__ = model.__dict__
                return True
        return False


# 程序开始的地方
view = DepView()
view.main()
