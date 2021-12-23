from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import DroneData, DroneType, PilotData

class DroneDateSerializer(serializers.ModelSerializer):
    class Meta:
        model=DroneData
        fields='__all__'
        # depth=1

class DroneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=DroneType
        fields='__all__'

class PilotDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=PilotData
        fields='__all__'

class UploadDroneDataSerializer(serializers.ModelSerializer):
    # drone_type=DroneTypeSerializer(many=False)
    # pilot=PilotDataSerializer(many=False)
    class Meta:
        model=DroneData
        fields='__all__'

class LocationDroneDataFetchSerializer(serializers.ModelSerializer):
    class Meta:
        model=DroneData
        fields=['reg_id', 'latitude', 'longitude']

class DroneDataMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model=DroneData
        fields=['drone_name','first_launch','total_flight_time_min','last_seen']