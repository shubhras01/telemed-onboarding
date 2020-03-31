from rest_framework_mongoengine.viewsets import ModelViewSet, GenericViewSet
from . models import Doctor
from . serializers import DoctorSerializer


class DoctorsViewSet(GenericViewSet):
    lookup_field = 'id'
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
