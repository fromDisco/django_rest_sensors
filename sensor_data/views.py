# import django modules/libraries
from django.shortcuts import render

# import rest_framework modules/libraries
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status
# exceptions for what might happen when creating a new value
from rest_framework.exceptions import ValidationError

# import app modules
from .models import SensorData
from .serializers import SensorDataSerializer


class SensorDataView(ListAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer


class RecieveSensorData(CreateAPIView):
    serializer_class = SensorDataSerializer

    def post(self, request, *args, **kwargs):
        print("___________")
        print(request.data)
        return self.create(request, *args, **kwargs)

