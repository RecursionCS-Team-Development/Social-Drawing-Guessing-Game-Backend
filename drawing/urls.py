from rest_framework import routers
from django.urls import path
from . import views

# router = routers.DefaultRouter()
# router.register(r'chatlog', views.ChatLogViewSet)

room_list = views.RoomViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

picture_list = views.PictureViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

chat_list = views.ChatLogViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('rooms/', room_list, name='room-list'),
    path('chat/', chat_list, name='chat'),
    path('pictures/', picture_list, name='picture-list'),
]
