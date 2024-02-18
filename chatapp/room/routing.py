from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path("ws/pc_master_race/", consumers.ChatConsumer.as_asgi()),
]
