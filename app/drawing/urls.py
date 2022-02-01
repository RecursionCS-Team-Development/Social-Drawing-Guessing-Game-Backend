from django.urls import path
from . import views

room_list = views.RoomViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

picture_list = views.PictureViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('rooms/', room_list, name='room-list'),
    path('pictures/', picture_list, name='picture-list'),
]
