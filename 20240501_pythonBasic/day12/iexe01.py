class EmployeeModel:
    def __init__(self, name, post, salary: float):
        self.name = name
        self.post = post
        self.salary = salary

    def __str__(self):
        return "姓名：%s，岗位：%s，工资：%s" % (self.name, self.post, self.salary)

    def __eq__(self, other):
        return self.name == other


class EmployeeController:
    def __init__(self):
        self.employee_list = []  # type: list[EmployeeModel]

    def add_employee(self, employee_model):
        self.employee_list.append(employee_model)

    def delete_employee(self, name):
        try:
            self.employee_list.remove(name)
            return True
        except:
            return False

    def update_employee(self, name):
        try:
            index_employee = self.employee_list.index(name)
            return index_employee
        except:
            return False


class EmployeeView:
    def __init__(self):
        self.__ctrl = EmployeeController()

    def main_menu(self):
        while True:
            print("1.添加员工")
            print("2.删除员工")
            print("3.修改员工")
            print("4.查询员工")
            print("5.退出系统")
            self.__select_menu()

    def __select_menu(self):
        num = input("请输入序号：")
        if num == '1':
            self.__input_emp()
        elif num == '2':
            self.__delete_emp()
        elif num == '3':
            self.__modify_emp()
        elif num == '4':
            self.__display_emp()
        else:
            exit('程序已经退出')

    def __input_emp(self):
        self.__ctrl.add_employee(
            EmployeeModel(input("请输入姓名："), input("请输入岗位："), float(input("请输入工资："))))

    def __delete_emp(self):
        name = input("请输入要删除的员工姓名：")
        info = self.__ctrl.delete_employee(name)
        if info:
            print("删除成功")
        else:
            print("删除失败")

    def __modify_emp(self):
        name = input("请输入要修改的员工姓名：")
        info = self.__ctrl.update_employee(name)
        if isinstance(info, int):
            self.__ctrl.employee_list[info].post = input("请输入新岗位：")
            self.__ctrl.employee_list[info].salary = float(input("请输入新工资："))
            print("修改成功")
        else:
            print("修改失败")

    def __display_emp(self):
        for item in self.__ctrl.employee_list:
            print(item)


if __name__ == '__main__':
    employee_view = EmployeeView()
    employee_view.main_menu()
