import jwt
from django.conf import settings
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Message, Room
from .serializers import ChatSerializer, MessageSerializer


class ChatView(mixins.CreateModelMixin,
               mixins.DestroyModelMixin,
               mixins.ListModelMixin,
               GenericViewSet):
    """
    View для Создания, удаления и получения чатов
    """
    serializer_class = ChatSerializer
    queryset = Room.objects.all()

    def perform_create(self, serializer):
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        if token:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload.get('user_id')
            user = User.objects.get(id=user_id)
            serializer.save(creator=user,
                            url="http://localhost:8000/chats/chats_manage/chats/")


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


def get_room_uuid(request, room_uuid):
    return JsonResponse({"id": Room.objects.get(uuid=room_uuid).pk})
