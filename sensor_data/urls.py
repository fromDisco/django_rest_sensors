from django.urls import path

from . import views

urlpatterns = [
    path("", views.SensorDataView.as_view()),
    path("send-data/", views.RecieveSensorData.as_view()),
]