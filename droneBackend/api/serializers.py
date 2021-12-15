from django.db import models
from django.db.models.base import Model
from rest_framework import serializers
from .models import DroneData, DroneType, PilotData

class DroneDateSerializer(serializers.ModelSerializer):
    class Meta:
        model=DroneData
        fields='__all__'

class DroneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=DroneType
        fields='__all__'

class UploadDroneDataSerializer(serializers.ModelSerializer):
    drone_type=DroneTypeSerializer(many=False)
    class Meta:
        model=DroneData
        fields='__all__'
