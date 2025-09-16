from django.urls import path
from .views import get_appointments

urlpatterns = [
    path('api/appointments/', get_appointments),
]
