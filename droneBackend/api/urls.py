from django.contrib import admin
from django.urls import path, include
from .views import main
from .views import UploadDroneDataView, DroneDataView, DroneTypeView, PilotDataView, LocationDroneDataFetchView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('dronedatashow/', DroneDataView.as_view()),
    path('dronetypeshow/', DroneTypeView.as_view()),
    path('pilotdatashow/',PilotDataView.as_view()),
    path('dronedata/',UploadDroneDataView.as_view()),
    path('locationfetch/', LocationDroneDataFetchView.as_view())
]