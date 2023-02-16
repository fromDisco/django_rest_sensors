from rest_framework import serializers
from .models import SensorData


class SensorDataSerializer(serializers.ModelSerializer):
    """
    This is some sample documentation which you can see in the browser
    """
    class Meta:
        model = SensorData
        fields = "__all__"
