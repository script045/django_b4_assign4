from django.db import models
from django.conf import settings
from donors.models import BLOOD_GROUPS

class BloodBank(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)

class DonationRequest(models.Model):
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    units = models.PositiveIntegerField(default=1)

    STATUS = [("pending","Pending"), ("approved","Approved"), ("rejected","Rejected")]
    status = models.CharField(max_length=10, choices=STATUS, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="approved_requests")
    approved_at = models.DateTimeField(null=True, blank=True)