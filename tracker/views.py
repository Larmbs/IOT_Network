from django.shortcuts import render
from ..devices.models import Device, fetch_device_sensors


# Views for main part of app that allows tracking
def home(request):
    return render(request, 'home.html')

def tracker(request):
    return render(request, 'tracker/tracker.html', {"device_list":Device.objects.all()})

def tracker_device_inspect(request, device_id):
    sensors = fetch_device_sensors(device_id)
    return render(request, 'tracker/device_inspect.html', {"device_list":Device.objects.all(), 'sensors':sensors})
    
def credits(request):
    return render(request, 'credits.html', {"device_list":Device.objects.all()})
