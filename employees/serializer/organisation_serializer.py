from rest_framework import serializers

from employees.models import Organisation


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields=["org_id","org_name","org_address"]
        read_only_fields=["org_id"]
