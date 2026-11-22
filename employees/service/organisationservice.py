from employees.Repository.organisation_repository import Organisation_repository

class OrganisationService:
    def __init__(self):
        self.organisation_repo=Organisation_repository()

    def create_organisation(self,data):
        return self.organisation_repo.create_organisation(data)

