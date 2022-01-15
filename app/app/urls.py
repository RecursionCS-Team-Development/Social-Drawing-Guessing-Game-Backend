from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/',include('djoser.urls'), name="auth"),
    path('api/auth/',include('djoser.urls.jwt')),
]
