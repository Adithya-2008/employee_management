from employees.models import EmploymentHistory


class EmploymentHistoryRepository:

    def create_employment_history(self, employee, organisation, data):
        return EmploymentHistory.objects.create(
            employee=employee,
            organisation=organisation,
            designation_name=data["designation_name"],
            employment_start_date=data["employment_start_date"],
            employment_end_date=data.get("employment_end_date")
        )

    '''def has_current_employment(self,employee):
        return EmploymentHistory.objects.filter(employee=employee,employment_end_date__isnull=True).exists()
'''

    def has_current_employment(self, employee):
        print("Checking employee:", employee.emp_id)

        current_employment = EmploymentHistory.objects.filter(
            employee_id=employee.emp_id,
            employment_end_date__isnull=True
        )

        print("Matching records:", current_employment.count())

        return current_employment.exists()
