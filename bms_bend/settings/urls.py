from django.urls import path, include
from rest_framework.routers import DefaultRouter
from donors.views import DonorProfileViewSet, DonationRecordViewSet
from blood.views import BloodBankViewSet, DonationRequestViewSet

router = DefaultRouter()
router.register("donors", DonorProfileViewSet)
router.register("records", DonationRecordViewSet)
router.register("banks", BloodBankViewSet)
router.register("requests", DonationRequestViewSet)

urlpatterns = [
    path("api/accounts/", include("accounts.urls")),
    path("api/", include(router.urls)),
]
