from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from employees.serializer.employee_serializer import EmployeeSerializer
from employees.service.employee_service import EmployeeService
from employees.schema.employee_schema import get_employees_schema


class EmployeeListView(GenericAPIView):

    def __init__(self):
        self.service = EmployeeService()

    @get_employees_schema
    def get(self, request):
        emp_ids=request.query_params.get('emp_ids')
        emp_ids=[int(emp_id) for emp_id in emp_ids.split(',')]
        employees=self.service.get_employee_by_ids(emp_ids)
        serializer=EmployeeSerializer(employees,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)




