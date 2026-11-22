from rest_framework import serializers
from employees.models.employee import Employee
from employees.serializer.employment_history_serializer import EmploymentHistorySerializer

class EmployeeDetailSerializer(serializers.ModelSerializer):

    employment_history = EmploymentHistorySerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Employee
        fields = [
            "emp_id",
            "name",
            "gender",
            "email",
            "phone_number",
            "date_of_birth",
            "employment_history"
        ]