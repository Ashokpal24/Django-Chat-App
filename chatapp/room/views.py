from .models import Room
from django.shortcuts import render
from .models import Message


def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})


def room(request, pk):
    room = Room.objects.get(pk=pk)
    messages = Message.objects.filter(room=room)[0:25]
    return render(request,
                  'room/room.html',
                  {
                      'room': room,
                      'messages': messages
                  })
