from django.db import models


class Vehicle(models.Model):
    VEHICLETYPE = (
        ('Two', 'Two'),
        ('Three', 'Three'),
        ('Four wheelers', 'Four wheelers')
    )
    vehicleNumber = models.CharField(max_length=15)
    vehicleType = models.CharField(max_length=15, choices=VEHICLETYPE)
    vehicleModel = models.CharField(max_length=50)
    vehicleDescription = models.TextField(max_length=500)

    def __str__(self):
        return self.vehicleNumber
