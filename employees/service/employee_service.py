from employees.Repository.employee_repository import EmployeeRepository


class EmployeeService:
    def __init__(self):
        self.employee_repo=EmployeeRepository()

    def create_employee(self,data):
        return self.employee_repo.create_employee(data)

    def get_employee_by_id(self,employee_id):
        return self.employee_repo.get_employee_with_history(employee_id)

    def get_employee_by_ids(self,emp_ids):
        return self.employee_repo.get_employee_by_ids(emp_ids)

    def get_employee_by_prev_organisation(self,org_id):
        return self.employee_repo.get_employee_by_prev_organisation(org_id)

    def get_employee_by_current_organisation(self,org_id):
        return self.employee_repo.get_employee_by_current_organisation(org_id)

    def get_employees_by_designation(self,org_id,designation):
        return self.employee_repo.get_employees_by_designation(org_id,designation)

    def get_employees_by_org_id(self,org_id):
        return self.employee_repo.get_employees_by_organisation(org_id)




    


