from django.contrib import admin
from .models import Device, Sensor, SensorDataFloat, SensorDataText

# Register your models here.
admin.site.register(Device)
admin.site.register(Sensor)
admin.site.register(SensorDataFloat)
admin.site.register(SensorDataText)