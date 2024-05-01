from django.db import models

# Create your models here.
class Device(models.Model):
    device_id = models.CharField(max_length=100)
    device_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.device_name + " " + self.device_id
    
"""Device Sensors"""
class Sensor(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    sensor_name = models.CharField(max_length=50)
    sensor_description = models.CharField(max_length=100)
    
    def __str__(self): 
        return f"{self.sensor_name} | {self.sensor_description}" 
    
class SensorDataText(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
    time = models.TimeField()
    
    def __str__(self):
        return f"[{self.sensor.sensor_name}]|{self.time.isoformat()}| {str(self.value)}"
    
class SensorDataFloat(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.FloatField()
    time = models.DateField()
    
    def __str__(self):
        return f"[{self.sensor.sensor_name}]|{self.time.isoformat()}| Value: {str(self.value)}"
    
"""Device Inputs"""