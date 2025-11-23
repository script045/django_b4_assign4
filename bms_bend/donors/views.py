from rest_framework import viewsets
from .models import DonorProfile, DonationRecord
from .serializers import DonorProfileSerializer, DonationRecordSerializer
from rest_framework.permissions import IsAuthenticated

class DonorProfileViewSet(viewsets.ModelViewSet):
    queryset = DonorProfile.objects.all()
    serializer_class = DonorProfileSerializer

class DonationRecordViewSet(viewsets.ModelViewSet):
    queryset = DonationRecord.objects.all()
    serializer_class = DonationRecordSerializer
