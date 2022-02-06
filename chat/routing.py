from django.urls import re_path
from . import consumers
from . import drawConsumers

# 本番の時wssに対応するようにしないといけない？
websocket_urlpatterns = [
  re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
  re_path(r'ws/draw/(?P<room_name>\w+)/$', drawConsumers.DrawConsumer.as_asgi())
]
