from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('chats/create_chat/<int:pk>', ChatCreateView.as_view())
]
