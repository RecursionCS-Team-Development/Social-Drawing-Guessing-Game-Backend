from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.

admin.site.register(User, UserAdmin)