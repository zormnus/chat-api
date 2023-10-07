from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    body = models.TextField()
    created_by = models.ForeignKey(User, blank=True, null=True,
                                   on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message "{self.body}" created by {self.created_by}'


class Room(models.Model):
    WAITING = 'waiting'
    ACTIVE = 'active'
    CLOSED = 'closed'

    ROOM_STATUS = (
        (WAITING, 'Waiting'),
        (ACTIVE, 'Active'),
        (CLOSED, 'Closed'),
    )

    uuid = models.CharField(max_length=255, unique=True)
    creator = models.ForeignKey(User, blank=True, null=True,
                                on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    messages = models.ManyToManyField(Message, blank=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=30, choices=ROOM_STATUS,
                              default=WAITING)

    def __str__(self):
        return f'Room {self.uuid}'
