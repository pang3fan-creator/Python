from dtl import EmployeeModel


class EmployeeController:
    def __init__(self):
        self.employee_list = []  # type: list[EmployeeModel]

    def add_employee(self, employee_model):
        self.employee_list.append(employee_model)

    def delete_employee(self, name):
        try:
            self.employee_list.remove(name)
            return True
        except ValueError:
            return False

    def update_employee(self, name):
        try:
            index_employee = self.employee_list.index(name)
            return index_employee
        except:
            return False
