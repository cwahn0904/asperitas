from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('firmware', views.firmware_upload, name='firmware'),
    path('get_latest_firmware', views.get_latest_firmware, name='get_latest_firmware'),
]