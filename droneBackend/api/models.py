from django.db import models

# Create your models here.

class DroneData(models.Model):
    drone_name=models.CharField(max_length=25, default="", unique=False, null=True)
    reg_id=models.IntegerField(null=False, default=0)
    last_seen=models.DateTimeField(null=True)
    first_launch=models.DateTimeField(null=True)
    total_flight_time=models.IntegerField(null=False, default=0)
    latitude=models.FloatField(null=False, default=0)
    longitude=models.FloatField(null=False, default=0)

class DroneType(models.Model):
    id=models.IntegerField(null=False,unique=True,primary_key=True)
    model_name=models.CharField(max_length=40, default="", unique=False)
    brand=models.CharField(max_length=40, default="", unique=False)
    model_year=models.IntegerField(null=False,unique=True)
    endurance_min=models.IntegerField(null=False,unique=True)
    sl_no=models.CharField(max_length=20, default="", unique=False)
    type=models.CharField(max_length=20, default="", unique=False)

class PilotData(models.Model):
    id=models.IntegerField(null=False,unique=True,primary_key=True)
    name=models.CharField(max_length=25, default="", unique=False, null=True)
    address=models.CharField(max_length=25, default="", unique=False, null=True)
    phone=models.BigIntegerField(null=True,unique=False)
    experience=models.IntegerField(null=True,unique=False)
    skill=models.IntegerField(null=True,unique=False)
    country=models.CharField(max_length=25, default="", unique=False, null=True)