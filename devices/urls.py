from django.urls import path

from . import views
from . import api_views

urlpatterns = [
    path('', views.home, name='home'),
    path('credits/', views.credits, name='credits'),
    path('tracker/', views.tracker, name='tracker'),
    path('tracker/<device_id>/inspect', views.tracker_device_inspect, name='tracker_inspect'),
    
    path('devices/create', api_views.DeviceCreateView.as_view(), name='device-create'),
    path('sensors/create', api_views.SensorCreateView.as_view(), name='sensor-create')

]