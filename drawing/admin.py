from django.contrib import admin
from .models import Room, Member, ChatLog, Picture
# Register your models here.


admin.site.register(Room)
admin.site.register(Member)
admin.site.register(ChatLog)
admin.site.register(Picture)