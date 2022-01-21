from django.urls import path
from .views import UserProfileCreateView

urlpatterns = [
    path('user', UserProfileCreateView.as_view(), name="user"),
]
