from django.db.models.fields import NullBooleanField
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DroneData, DroneType, PilotData
from .serializers import DroneDateSerializer, UploadDroneDataSerializer, DroneTypeSerializer, PilotDataSerializer

# Create your views here.

def main(request):
    return HttpResponse("firddd")

class DroneDataView(generics.ListCreateAPIView):
    queryset=DroneData.objects.all()
    serializer_class=DroneDateSerializer

class DroneTypeView(generics.ListCreateAPIView):
    queryset=DroneType.objects.all()
    serializer_class=DroneTypeSerializer

class PilotDataView(generics.ListCreateAPIView):
    queryset=PilotData.objects.all()
    serializer_class=PilotDataSerializer

class UploadDroneDataView(APIView):
    serializer_class=UploadDroneDataSerializer
    
    def post(self, request):
        #need to improve this into create() or update() or an other in serializer
        for data in request.data:
            e=data.pop('location')
            data.update(e)
            
            dronetype=data.pop('drone_type')
            pilotdata=data.pop('pilot')
            # drone type is searched and updated
            queryset=DroneType.objects.all().filter(id=dronetype['id'])
            if queryset.exists():
                pass
            else:
                print('new')
                dronetypeserializer=DroneTypeSerializer(data=dronetype)
                if dronetypeserializer.is_valid():
                    dronetypeserializer.save()
            data['drone_type']=dronetype['id']
            
            # pilot data is seartched and updated one by one
            queryset=PilotData.objects.filter(id=pilotdata['id'])
            if queryset.exists():
                pass
            else:
                print('new pilot data encounterd')
                pilotdataserializer=PilotDataSerializer(data=pilotdata)
                if pilotdataserializer.is_valid():
                    pilotdataserializer.save()
            data['pilot']=pilotdata['id']
        
        # entire drone data is updated
        for data in request.data:
            queryset=DroneData.objects.filter(reg_id=data['reg_id'])
            if queryset.exists():
                dronedata=queryset[0]
                if dronedata.drone_type==NullBooleanField:
                    dronedata.drone_type=DroneType.objects.get(id=data['drone_type'])
                    dronedata.save(update_fields=['drone_type'])
                # must add if condition ie not null or not present in database or not
                print(queryset[0],'pilot data set for each drone')
                dronedata.pilot=PilotData.objects.get(id=data['pilot'])
                dronedata.save(update_fields=['pilot'])
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