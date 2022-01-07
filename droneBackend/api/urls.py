from django.contrib import admin
from django.urls import path, include
from .views import main
from .views import UploadDroneDataView, DroneDataView, DroneTypeView, PilotDataView, LocationDroneDataFetchView
from .views import FetchDroneDataByID, FetchDroneDataByType

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('dronedatashow/', DroneDataView.as_view()),
    path('dronetypeshow/', DroneTypeView.as_view()),
    path('pilotdatashow/',PilotDataView.as_view()),
    path('dronedata/',UploadDroneDataView.as_view()),
    path('locationfetch/', LocationDroneDataFetchView.as_view()),
    path('dronedataID/<str:ID>/',FetchDroneDataByID.as_view()),
    path('dronedatatype/<str:Type>/',FetchDroneDataByType.as_view())
]