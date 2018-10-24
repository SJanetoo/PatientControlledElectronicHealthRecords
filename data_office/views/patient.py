from data_office.models import Patient
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from data_office.serializers import (
    PatientListSerializer,
    PatientResetSerializer,
    PatientSignupSerializer
)

 
class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientListSerializer


class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientResetSerializer

    def get_queryset(self):
        return Patient.objects.all().filter(user=self.request.user)


class PatientCreation(generics.CreateAPIView):
    serializer_class = PatientSignupSerializer
