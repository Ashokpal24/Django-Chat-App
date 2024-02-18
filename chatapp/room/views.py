from .models import Room
from django.shortcuts import render


def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})


def room(request, pk):
    room = Room.objects.get(pk=pk)

    return render(request, 'room/room.html', {'room': room})
