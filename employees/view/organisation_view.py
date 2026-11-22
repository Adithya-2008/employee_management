from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from employees.serializer.organisation_serializer import OrganisationSerializer
from employees.service.organisationservice import OrganisationService

class OrganisationView(GenericAPIView):
    serializer_class = OrganisationSerializer

    def __init__(self):
        self.service=OrganisationService()

    def post(self,request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        organisation=self.service.create_organisation(serializer.validated_data)
        response_serializer=self.get_serializer(organisation)
        return Response(response_serializer.data,status=status.HTTP_201_CREATED)


