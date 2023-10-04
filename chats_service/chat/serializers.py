from rest_framework import serializers
from .models import Message, Room
from rest_framework_simplejwt.tokens import RefreshToken


class ChatSerializer(serializers.ModelSerializer):
    uuid = serializers.CharField()
    status = serializers.CharField()

    class Meta:
        model = Room
        fields = ('uuid', 'status')

    def create(self, validated_data):
        return super().create(validated_data)
