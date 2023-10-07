from django.urls import include, path
from rest_framework import routers

from .views import ChatView, RoomMessages

router = routers.SimpleRouter()
router.register(r'chats', ChatView)

urlpatterns = [
    path('chats_manage/', include(router.urls)),
    path('chat_messages/<str:room_uuid>/', RoomMessages.as_view()),
]
