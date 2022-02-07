from rest_framework import serializers
from .models import Room, Member, ChatLog, Picture

from accounts.serializers import UserSerializer


class RoomSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()
    class Meta:
        model = Room
        fields = ('id', 'name', 'password', 'entryNum', 'mode', 'level', 'round', 'members')

    def get_members(self, obj):
        try:
            member_content = MemberSerializer(Member.objects.all().filter(room=Room.objects.get(id=obj.id)), many=True).data
            return member_content
        except:
            member_content = None
            return member_content

class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Member
        fields = ('id', 'room', 'user', 'score')


class ChatLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatLog
        fields = ('id', 'member', 'message')



class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'created_by', 'created_at', 'img')
