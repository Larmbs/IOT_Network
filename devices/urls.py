from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('credits/', views.credits, name='credits'),
    path('tracker/', views.tracker, name='tracker'),
    path('tracker/<device_id>/inspect', views.tracker_device_inspect, name='tracker_inspect')
]