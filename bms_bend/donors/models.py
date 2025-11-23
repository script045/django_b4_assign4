from django.db import models
from django.conf import settings

BLOOD_GROUPS = [
    ("A+", "A+"), 
    ("A-", "A-"),
    ("B+", "B+"), 
    ("B-", "B-"),
    ("O+", "O+"), 
    ("O-", "O-"),
    ("AB+", "AB+"), 
    ("AB-", "AB-")
]

class DonorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=120)
    last_donation = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profiles/", blank=True, null=True)


class DonationRecord(models.Model):
    donor = models.ForeignKey(DonorProfile, on_delete=models.CASCADE, related_name="records")
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    units = models.PositiveIntegerField(default=1)
    date = models.DateField(auto_now_add=True)
    note = models.TextField(blank=True)
    
    def __str__(self):
        return f"Donation by {self.donor.user.username} on {self.date}"