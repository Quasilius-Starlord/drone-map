from django.contrib import admin
from django.urls import path, include
from .views import main
from .views import UploadDroneDataView, DroneDataView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('dronedata/',UploadDroneDataView.as_view()),
    path('', main)
]