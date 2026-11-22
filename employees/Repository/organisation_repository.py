from employees.models.organisation import Organisation

class Organisation_repository:
    def create_organisation(self, data):
        return Organisation.objects.create(**data)

    def get_organisation_by_id(self, id):
        return Organisation.objects.get(org_id=id)

