from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DroneData, DroneType, PilotData
from .serializers import DroneDateSerializer, UploadDroneDataSerializer, DroneTypeSerializer

# Create your views here.

def main(request):
    return HttpResponse("firddd")

class DroneDataView(generics.ListCreateAPIView):
    queryset=DroneData.objects.all()
    serializer_class=DroneDateSerializer

class DroneTypeView(generics.ListCreateAPIView):
    queryset=DroneType.objects.all()
    serializer_class=DroneTypeSerializer

class UploadDroneDataView(APIView):
    serializer_class=UploadDroneDataSerializer
    
    def post(self, request):
        #need to improve this into create() or update() or an other in serializer
        for data in request.data:
            e=data.pop('location')
            data.update(e)
            
            dronetype=data.pop('drone_type')
            queryset=DroneType.objects.all().filter(id=dronetype['id'])
            if queryset.exists():
                pass
            else:
                print('new')
                dronetypeserializer=DroneTypeSerializer(data=dronetype)
                if dronetypeserializer.is_valid():
                    dronetypeserializer.save()
            data['drone_type']=dronetype['id']

        # serializer=self.serializer_class(data=request.data, many=True)
        for data in request.data:
            queryset=DroneData.objects.filter(reg_id=data['reg_id'])
            if queryset.exists():
                print(queryset[0])
                dronedata=queryset[0]
                dronedata.drone_type=DroneType.objects.get(id=data['drone_type'])
                dronedata.save(update_fields=['drone_type'])
            else:
                serializer=self.serializer_class(data=data)
                serializer.save()
        # print('efefe',type(request.data[0]))
        print(request.data[0],end="\n\n")
        
        # if serializer.is_valid():
        #     pass
        #     # print('nameeeeeeeeeeeee',serializer.data)
        #     # serializer.save()
        # else:
        #     print('INVALID')
        #     print('nameeeeeeeeeeeee',serializer.data)
        #     return Response({}, status=status.HTTP_304_NOT_MODIFIED)
        return Response({}, status=status.HTTP_200_OK)