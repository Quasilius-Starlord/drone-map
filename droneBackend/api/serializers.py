from django.db.models.base import Model
from rest_framework import serializers
from .models import DroneData

class DroneDateSerializer(serializers.ModelSerializer):
    class Meta:
        model=DroneData
        fields='__all__'

class UploadDroneDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=DroneData
        fields=('drone_name','reg_id','last_seen','first_launch','total_flight_time','latitude','longitude')