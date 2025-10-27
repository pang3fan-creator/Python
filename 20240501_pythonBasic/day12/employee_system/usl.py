from bll import EmployeeController
from dtl import EmployeeModel


class EmployeeView:
    def __init__(self):
        self.controller = EmployeeController()

    def display_menu(self):
        print("1.添加员工")
        print("2.删除员工")
        print("3.修改员工")
        print("4.查询员工")
        print("5.退出系统")
        self.select_menu()

    def select_menu(self):
        num = input("请输入序号：")
        if num == '1':
            self.input_employee()
        elif num == '2':
            self.delete_employee()
        elif num == '3':
            self.modify_employee()
        elif num == '4':
            self.display_employee()
        else:
            exit('程序已经退出')

    def input_employee(self):
        employee_model = EmployeeModel(input("请输入姓名："),
                                       input("请输入岗位："),
                                       float(input("请输入工资：")))
        self.controller.add_employee(employee_model)

    def delete_employee(self):
        name = input("请输入要删除的员工姓名：")
        info = self.controller.delete_employee(name)
        if info:
            print("删除成功")
        else:
            print("删除失败")

    def modify_employee(self):
        name = input("请输入要修改的员工姓名：")
        info = self.controller.update_employee(name)
        if isinstance(info, int):
            self.controller.employee_list[info].post = input("请输入新岗位：")
            self.controller.employee_list[info].salary = float(input("请输入新工资："))
            print("修改成功")
        else:
            print("修改失败")

    def display_employee(self):
        for item in self.controller.employee_list:
            print(item)
