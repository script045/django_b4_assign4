from rest_framework import serializers
from .models import BloodBank, DonationRequest

class BloodBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodBank
        fields = "__all__"

class DonationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationRequest
        fields = "__all__"
        read_only_fields = ["status", "approved_by", "requester"]
