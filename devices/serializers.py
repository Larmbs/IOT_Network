from rest_framework import serializers
from .models import Device, Sensor, SensorDataText, SensorDataFloat

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class SensorDataTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorDataText
        fields = '__all__'

class SensorDataFloatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorDataFloat
        fields = '__all__'
