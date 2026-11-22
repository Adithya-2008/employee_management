from employees.models import employment_history
from employees.models.employee import Employee
from employees.models.employment_history import EmploymentHistory


class EmployeeRepository:

    def create_employee(self,data):
        return Employee.objects.create(**data)

    def get_employee_by_id(self,employee_id):
        return Employee.objects.get(emp_id=employee_id)

    def get_employee_with_history(self,employee_id):
        return Employee.objects.prefetch_related("employment_history").get(emp_id=employee_id)

    def get_employee_by_ids(self,emp_ids):
        return Employee.objects.filter(emp_id__in=emp_ids)

    def get_employee_by_prev_organisation(self, org_id):
        return Employee.objects.filter(
            employment_history__organisation_id=org_id,
            employment_history__employment_end_date__isnull=False
        ).distinct()

    def get_employee_by_current_organisation(self,org_id):
        return Employee.objects.filter(
            employment_history__organisation_id=org_id,
            employment_history__employment_end_date__isnull=True
        ).distinct()

    def get_employees_by_designation(self, org_id, designation):
        return Employee.objects.filter(
            employment_history__organisation_id=org_id,
            employment_history__designation_name=designation,
            employment_history__employment_end_date__isnull=True
        ).distinct()

    def get_employees_by_organisation(self, org_id):
        return Employee.objects.filter(
            employment_history__organisation_id=org_id
        ).distinct()