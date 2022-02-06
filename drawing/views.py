from django.http import HttpResponse
from rest_framework import filters, viewsets
from .models import Room, Member, ChatLog, Picture
from .serializers import RoomSerializer, MemberSerializer, ChatLogSerializer, PictureSerializer

# test
def IndexView(request):
  return HttpResponse("Hello World")


class RoomViewSet(viewsets.ModelViewSet):
  queryset = Room.objects.all()
  serializer_class = RoomSerializer
  filter_backends = (filters.OrderingFilter,)
  ordering_fields = ('id', 'mode', 'level',)
  ordering = ('id')


class MemberViewSet(viewsets.ModelViewSet):
  queryset = Member.objects.all()
  serializer_class = MemberSerializer
  filter_backends = (filters.OrderingFilter,)
  ordering_fields = ('id', 'room', 'is_play',)
  ordering = ('id')

class ChatLogViewSet(viewsets.ModelViewSet):
  queryset = ChatLog.objects.all()
  serializer_class = ChatLogSerializer
  filter_backends = (filters.OrderingFilter,)
  ordering_fields = ('id',)
  ordering = ('id')

class PictureViewSet(viewsets.ModelViewSet):
  queryset = Picture.objects.all()
  serializer_class = PictureSerializer
  filter_backends = (filters.OrderingFilter,)
  ordering_fields = ('id', 'created_by', 'created_at')
  ordering = ('created_at')
