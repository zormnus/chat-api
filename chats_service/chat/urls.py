from django.urls import include, path
from rest_framework import routers

from .views import ChatsView, RoomMessages

router = routers.SimpleRouter()
router.register(r'chats', ChatsView)

urlpatterns = [
    path('chats_manage/', include(router.urls)),
    path('chat_messages/<str:room_uuid>/', RoomMessages.as_view()),
]
