from django.db.models import query
from django.db.models.fields import NullBooleanField
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DroneData, DroneType, PilotData
from .serializers import DroneDateSerializer, UploadDroneDataSerializer, DroneTypeSerializer, PilotDataSerializer, LocationDroneDataFetchSerializer, DroneDataMinimalSerializer
import json
from shapely.geometry import Point, Polygon

# Create your views here.

def main(request):
    return HttpResponse("firddd")

class DroneDataView(generics.ListCreateAPIView):
    queryset=DroneData.objects.order_by('last_seen').all()
    serializer_class=DroneDateSerializer

class FetchDroneDataByID(generics.ListCreateAPIView):
    serializer_class=DroneDateSerializer
    def list(self, request, ID):
        print(ID)
        try:
            queryset=DroneData.objects.get(reg_id=ID)
            serializer=self.serializer_class(queryset)
            print(serializer.data)
            return Response(serializer.data)
        except:
            return Response({})

class FetchDroneDataByType(generics.ListCreateAPIView):
    serializer_class=DroneDateSerializer
    def list(self, request, Type):
        print(Type)
        try:
            queryset=DroneType.objects.get(model_name=Type)
            serialiser=DroneTypeSerializer(queryset)
            typeId=serialiser.data['id']
            queryset=DroneData.objects.filter(drone_type=typeId)
            if queryset.exists():
                serialiser=DroneDateSerializer(queryset, many=True)
                return Response(serialiser.data)
            else:
                raise Exception('error')
        except :
            return Response({})

    def get_queryset(self):
        print(self.request)
        return DroneData.objects.all()

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
        return Response({}, status=status.HTTP_200_OK)
        droneDataset=json.loads(request.data.get('file'))
        print(droneDataset, type(droneDataset))
        for data in droneDataset:
            e=data.pop('location')
            data.update(e)
            
            dronetype=data.pop('drone_type')
            pilotdata=data.pop('pilot')
            # drone type is searched and updated
            queryset=DroneType.objects.all().filter(id=dronetype['id'])
            if queryset.exists():
                pass
            else:
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
        for data in droneDataset:
            queryset=DroneData.objects.filter(reg_id=data['reg_id'])
            if queryset.exists():
                dronedata=queryset[0]
                if dronedata.drone_type==None:
                    dronedata.drone_type=DroneType.objects.get(id=data['drone_type'])
                    dronedata.save(update_fields=['drone_type'])
                if dronedata.pilot==None:
                    dronedata.pilot=PilotData.objects.get(id=data['pilot'])
                    dronedata.save(update_fields=['pilot'])
            else:
                print(data, DroneType.objects.get(id=data['drone_type']))
                serializer=self.serializer_class(data=data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print('INVALID')
        
        return Response({}, status=status.HTTP_200_OK)

class LocationDroneDataFetchView(APIView):
    serializer_class=LocationDroneDataFetchSerializer
    drone_data_serializer_class=DroneDataMinimalSerializer

    def post(self, request):
        print(request.data['polygon'])
        droneData=DroneData.objects.all()
        polygon=[]
        for coord in request.data['polygon']:
            polygon.append((coord[0], coord[1]))
        polygon=Polygon(polygon)
        print(polygon)
        # polygon is for the polygon bounded box
        validID=[];
        for drone in droneData:
            serializer=self.serializer_class(drone)
            point=Point(serializer.data['latitude'],serializer.data['longitude'])
            if point.within(polygon):
                validID.append(serializer.data['reg_id'])
                pass
            pass
        print(validID)
        dataset=[]
        droneData=DroneData.objects.filter(reg_id__in=validID)
        for drone in droneData:
            serializer=self.drone_data_serializer_class(drone)
            dataset.append(serializer.data)
        
        return Response(json.dumps({'data':dataset}), content_type="application/json", status=status.HTTP_200_OK)
