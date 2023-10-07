from django.urls import include, path
from rest_framework import routers

from .views import ChatView, RoomMessages, get_room_uuid

router = routers.SimpleRouter()
router.register(r'chats', ChatView)

urlpatterns = [
    path('chats_manage/', include(router.urls)),
    path('chat_messages/<str:room_uuid>/', RoomMessages.as_view()),
    path('chat/id/<str:room_uuid>', get_room_uuid),
]
