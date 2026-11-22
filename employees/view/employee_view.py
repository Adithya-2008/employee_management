from django.core.serializers import get_serializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from employees.serializer.employee_serializer import EmployeeSerializer
from employees.serializer.employment_detail_serializer import EmployeeDetailSerializer
from employees.service.employee_service import EmployeeService


class EmployeeCreateView(GenericAPIView):
    serializer_class = EmployeeSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = EmployeeService()

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employee = self.service.create_employee(serializer.validated_data)
        response_serializer = self.get_serializer(employee)
        return Response(response_serializer.data,status=status.HTTP_201_CREATED)

class EmployeeDetailView(GenericAPIView):
    serializer_class = EmployeeSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = EmployeeService()

    def get(self, request, emp_id):
        employee = self.service.get_employee_by_id(emp_id)
        response_serializer = EmployeeDetailSerializer(employee)
        return Response(response_serializer.data,status=status.HTTP_200_OK)

class EmployeeByPreviousOrganisationView(GenericAPIView):
    serializer_class = EmployeeSerializer

    def __init__(self):
        self.service=EmployeeService()

    def get(self,request,org_id):
        employees=self.service.get_employee_by_prev_organisation(org_id)
        response_serializer=self.get_serializer(employees,many=True)
        return Response(response_serializer.data,status=status.HTTP_200_OK)

class EmployeeByCurrentOrganisationView(GenericAPIView):
    serializer_class = EmployeeSerializer

    def __init__(self):
        self.service=EmployeeService()

    def get(self,request,org_id):
        employees=self.service.get_employee_by_current_organisation(org_id)
        response_serializer=self.get_serializer(employees,many=True)
        return Response(response_serializer.data,status=status.HTTP_200_OK)

class EmployeeByDesignationView(GenericAPIView):
    serializer_class = EmployeeSerializer

    def __init__(self):
        self.service=EmployeeService()

    def get(self,request,org_id,designation):
        employees=self.service.get_employees_by_designation(org_id,designation)
        response_serializer=self.get_serializer(employees,many=True)
        return Response(response_serializer.data,status=status.HTTP_200_OK)



class EmployeeByOrganisationView(GenericAPIView):
    serializer_class = EmployeeSerializer

    def __init__(self):
        self.service = EmployeeService()

    def get(self, request, org_id):
        employees = self.service.get_employees_by_org_id(org_id)
        serializer = self.get_serializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

