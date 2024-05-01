from django.shortcuts import render
from .models import Device

# Create your views here.
def home(request):
    return render(request, 'home.html')

def tracker(request):
    return render(request, 'tracker/tracker.html', {"device_list":Device.objects.all()})

def tracker_device_inspect(request):
    device_id = request.Get.get()
    

def credits(request):
    return render(request, 'credits.html', {"device_list":Device.objects.all()})
