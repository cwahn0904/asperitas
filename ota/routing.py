from django.urls import path, include
from . import consumers

websocket_urlpatterns = [
    path('ws/ota/', consumers.ContConsumer.as_asgi()),
]