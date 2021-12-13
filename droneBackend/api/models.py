from django.db import models

# Create your models here.

class DroneData(models.Model):
    name=models.CharField(max_length=25, default="", unique=False, null=True)
    reg_id=models.IntegerField(null=False, default=0)
    last_seen=models.DateTimeField(null=True)
    first_launch=models.DateTimeField(null=True)
    total_flight_time=models.IntegerField(null=False, default=0)