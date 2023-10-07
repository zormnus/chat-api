from rest_framework import serializers

from .models import Message, Room


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("uuid", "created_at", )


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("body", "created_by", )
