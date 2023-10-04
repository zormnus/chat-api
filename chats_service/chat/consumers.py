from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from .models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(self.room_group_name,
                                           self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name,
                                               self.channel_name)

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "chat.message", "message": text_data}
        )

    async def chat_message(self, event):
        await self.send(text_data=event["message"])

    @sync_to_async
    def message_create(self, message_body, create_by, creator):
        message = Message.objects.create(
            body=message_body, create_by=create_by, creator=creator
        )
        message.save()
