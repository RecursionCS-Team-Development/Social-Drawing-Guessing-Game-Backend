from django.urls import path
from .views import UserProfileCreateView, LoginAPIView

urlpatterns = [
    # path('login', LoginAPIView.as_view(), name="login"),
    path('user', UserProfileCreateView.as_view(), name="user"),
]
