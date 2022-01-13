from django.contrib.auth import get_user_model
from rest_framework import viewsets

from accounts.serializers import UserSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
