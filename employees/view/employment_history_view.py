from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from employees.serializer.employment_history_serializer import EmploymentHistorySerializer
from employees.service.employee_history_service import EmployeeHistoryService


class EmploymentHistoryView(GenericAPIView):
    serializer_class = EmploymentHistorySerializer

    def __init__(self):
        self.service = EmployeeHistoryService()

    def post(self, request, emp_id):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employment_history = self.service.create_employment_history(emp_id,serializer.validated_data)
        response_serializer = self.get_serializer(employment_history)
        return Response(response_serializer.data,status=status.HTTP_201_CREATED)