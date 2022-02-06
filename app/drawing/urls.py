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

member_list = views.MemberViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update',
})

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('rooms/', room_list, name='room-list'),
    path('members/', member_list, name='member-list'),
    path('pictures/', picture_list, name='picture-list'),
]
