class EmployeeModel:
    def __init__(self, name, ):
        self.name = name


class EmployeeController:
    def __init__(self, name):
        self.employee_list = []  # type: list[EmployeeModel]
        self.name = name


class EmployeeView:
    def __init__(self, name):
        self.ctrl = EmployeeController(2)
        self.name = name

    def input_emp(self):
        model = EmployeeModel(input("姓名："))
        self.ctrl.employee_list.append(model)


employee_view = EmployeeView(1)

while True:
    employee_view.input_emp()
