from employees.Repository.employee_repository import EmployeeRepository
from employees.Repository.employee_history_repository import EmploymentHistoryRepository
from employees.Repository.organisation_repository import Organisation_repository
from employees.models import Employee, Organisation

class EmployeeHistoryService:
    def __init__(self):
        self.employee_history_repo=EmploymentHistoryRepository()
        self.employee_repo = EmployeeRepository()
        self.organisation_repo=Organisation_repository()

    def create_employment_history(self,emp_id,data):
        try:
            employee=self.employee_repo.get_employee_by_id(emp_id)
        except Employee.DoesNotExist:
            raise ValueError('Employee with id {} does not exist'.format(emp_id))
        org_id=data['org_id']

        try:
            organisation=self.organisation_repo.get_organisation_by_id(org_id)
        except Organisation.DoesNotExist:
            raise ValueError('Organisation with id {} does not exist'.format(org_id))
        '''
        if data.get('employment_end_date') is None:
            current_employment=self.employee_history_repo.has_current_employment(employee)
            if current_employment:
                raise ValueError("Employee already has a current organisation")
        '''
        print("Validated data:", data)
        print("End date value:", repr(data.get('employment_end_date')))
        print("Is None:", data.get('employment_end_date') is None)
        if data.get('employment_end_date') is None:
            print("End date is NULL")

            current_employment = self.employee_history_repo.has_current_employment(employee)

            print("Current employment exists:", current_employment)

            if current_employment:
                raise ValueError("Employee already has a current organisation")
        return self.employee_history_repo.create_employment_history(employee,organisation,data)




