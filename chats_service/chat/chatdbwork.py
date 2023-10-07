from asgiref.sync import sync_to_async

from .models import Room


@sync_to_async
def get_room(room_id):
    return Room.objects.get(uuid=room_id)


# @sync_to_async
# def create_room():
#     Room.objects.create()