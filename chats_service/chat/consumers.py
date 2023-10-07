import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from django.http.response import Http404
from django.shortcuts import get_object_or_404

from .models import Message, Room


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        self.bd_room = await self.get_room(self.room_name)

        await self.channel_layer.group_add(self.room_group_name,
                                           self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name,
                                               self.channel_name)

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "chat_message", "message": text_data}
        )

    async def chat_message(self, event):
        decoded_message = event["message"]
        saved_message = await self.message_create(
            message_body=decoded_message,
            created_by=self.scope['user'])
        await self.room_extend(saved_message)
        await self.send(text_data=decoded_message)

    @sync_to_async
    def message_create(self, message_body, created_by):
        message = Message.objects.create(
            body=message_body, created_by=created_by
        )
        message.save()
        return message

    @sync_to_async
    def get_room(self, room_id):
        return Room.objects.get(uuid=room_id)

    @sync_to_async
    def get_user_id(self, username) -> User:
        return User.objects.get(username=username)

    @sync_to_async
    def room_extend(self, message):
        self.bd_room.messages.add(message)
