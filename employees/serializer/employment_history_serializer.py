from rest_framework import serializers
from employees.models import EmploymentHistory


class EmploymentHistorySerializer(serializers.ModelSerializer):

    org_id = serializers.IntegerField(write_only=True)
    org_name = serializers.CharField(
        source='organisation.org_name',
        read_only=True
    )

    class Meta:
        model = EmploymentHistory
        fields = [
            "id",
            "org_id",
            "org_name",
            "designation_name",
            "employment_start_date",
            "employment_end_date"
        ]
        read_only_fields = ["id"]