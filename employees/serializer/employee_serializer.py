from rest_framework import serializers

from employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields = [
            "emp_id",
            "name",
            "gender",
            "email",
            "phone_number",
            "date_of_birth"
        ]
        read_only_fields = ["emp_id"]
