from django.contrib import admin
from django.urls import path, include
from .views import main
from .views import DroneDataView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('dronedata/',DroneDataView.as_view()),
    path('', main)
]