from django.urls import path
from . import views

picture_list = views.PictureViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('pictures/', picture_list, name='picture-list'),
]
