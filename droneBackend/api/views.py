from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.view import APIView
from .models import DroneData
from .serializers import DroneDateSerializer, UploadDroneDataSerializer

# Create your views here.

def main(request):
    return HttpResponse("firddd")

class DroneDataView(generics.ListAPIView):
    queryset=DroneData.objects.all()
    serializer_class=DroneDateSerializer

class UploadDroneDataView(APIView):
    serializer_class=UploadDroneDataSerializer
    
    def post(self, request, format=None):
        serializer=self.serializer_class(data=request.data)
        if serializer.isvalid():
            dronedata=DroneData(name=serializer.data.name, )