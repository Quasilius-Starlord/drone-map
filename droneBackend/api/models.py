from django.db import models
from django.db.models.deletion import CASCADE, PROTECT

# Create your models here.

class DroneType(models.Model):
    id=models.IntegerField(null=False,unique=True,primary_key=True)
    model_name=models.CharField(max_length=40, default="", unique=False)
    brand=models.CharField(max_length=40, default="", unique=False)
    model_year=models.CharField(max_length=10,null=True,unique=False)
    endurance_min=models.CharField(max_length=20,null=True,default="",unique=False)
    sl_no=models.CharField(max_length=20, null=True, default="", unique=False)
    type=models.CharField(max_length=20, null=True, default="", unique=False)

class PilotData(models.Model):
    id=models.IntegerField(null=False,unique=True,primary_key=True)
    name=models.CharField(max_length=25, default="", unique=False, null=True)
    address=models.CharField(max_length=50, default="", unique=False, null=True)
    phone=models.CharField(max_length=15, default="", unique=False, null=True)
    experience=models.IntegerField(null=False,unique=False,default=0)
    skill=models.IntegerField(null=False,unique=False,default=0)
    country=models.CharField(null=False,max_length=25, default="India", unique=False)

class DroneData(models.Model):
    drone_name=models.CharField(max_length=25, default="", unique=False, null=True)
    reg_id=models.IntegerField(primary_key=True, unique=True ,null=False)
    last_seen=models.DateTimeField(null=True)
    first_launch=models.DateTimeField(null=True)
    total_flight_time_min=models.IntegerField(null=False, default=0)
    latitude=models.FloatField(null=False, default=0)
    longitude=models.FloatField(null=False, default=0)
    drone_type=models.ForeignKey(DroneType,on_delete=CASCADE, null=True)
    pilot=models.ForeignKey(PilotData,on_delete=CASCADE, null=True)