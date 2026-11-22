from django.db import models

from employees.models.employee import Employee
from employees.models.organisation import Organisation


class EmploymentHistory(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='employment_history')
    organisation = models.ForeignKey(Organisation,on_delete=models.CASCADE,related_name='employment_history')
    employment_start_date = models.DateField()
    employment_end_date = models.DateField(null=True, blank=True)
    designation_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'employment_history'