from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DroneData
from .serializers import DroneDateSerializer, UploadDroneDataSerializer

# Create your views here.

def main(request):
    return HttpResponse("firddd")

class DroneDataView(generics.ListCreateAPIView):
    queryset=DroneData.objects.all()
    serializer_class=DroneDateSerializer

class UploadDroneDataView(APIView):
    serializer_class=UploadDroneDataSerializer
    
    def post(self, request):
        #need to improve this into create() or update() or an other in serializer
        for data in request.data:
            e=data.pop('location')
            data.update(e)
        
        serializer=self.serializer_class(data=request.data, many=True)
        print('efefe',type(request.data[0]))
        # print(request.data[0])
        
        if serializer.is_valid():
            print('nameeeeeeeeeeeee',serializer.data)
            serializer.save()
            # dronedata=DroneData(name=serializer.data.get('name'),total_flight_time=serializer.data.get('total_flight_time'))
            # dronedata.save()
        else:
            return Response({}, status=status.HTTP_400)
        return Response({}, status=status.HTTP_200_OK)