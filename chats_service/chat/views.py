from django.http import JsonResponse
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Message, Room
from .serializers import ChatSerializer, MessageSerializer


class ChatsView(mixins.CreateModelMixin,
                mixins.DestroyModelMixin,
                mixins.ListModelMixin,
                GenericViewSet):
    """
    View для Создания, удаления и получения чатов
    """
    serializer_class = ChatSerializer
    queryset = Room.objects.all()


class MessageView(mixins.CreateModelMixin,
                  GenericViewSet):
    """
    View для создания сообщений
    """
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class RoomMessages(APIView):
    """
    View для получения всех сообщений из определённого чата
    """
    def get(self, request, room_uuid):
        room = Room.objects.get(uuid=room_uuid)
        messages = list(room.messages.values('body', 'created_by__username',
                                             'created_at'))
        return JsonResponse({"messages": messages})
