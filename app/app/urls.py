from django.contrib import admin
from django.urls import path, include
import drawing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/',include('djoser.urls'), name="auth"),
    path('api/auth/',include('djoser.urls.jwt')),
    path('test/', include('drawing.urls'), name="index"),
    # path('api/', include('drawing.urls')),
]
