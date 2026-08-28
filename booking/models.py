from django.db import models


class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    booking_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.service}"