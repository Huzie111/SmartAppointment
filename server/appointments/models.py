from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

# Custom User model
class User(AbstractUser):
    is_provider = models.BooleanField(default=False)  # True if service provider
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username


class Service(models.Model):
    provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="services")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    duration = models.DurationField(help_text="e.g. 30 minutes")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} by {self.provider.username}"


class Appointment(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="appointments")
    provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="provided_appointments")
    appointment_date = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("confirmed", "Confirmed"),
            ("cancelled", "Cancelled"),
            ("completed", "Completed"),
        ],
        default="pending"
    )
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.client.username} - {self.service.name} on {self.appointment_date}"
