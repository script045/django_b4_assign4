from rest_framework import serializers
from .models import DonorProfile, DonationRecord

class DonorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorProfile
        fields = "__all__"

class DonationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationRecord
        fields = "__all__"
