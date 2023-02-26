from django.shortcuts import render
from .models import Room

# Create your views here.

'''
rooms = [
    {'id':1, 'name':'Python'},
    {'id':2, 'name':'C++'},
    {'id':3, 'name':'Matplotlib'},
    {'id':4, 'name':'Pandas'},
]
'''


def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'base/room.html', context)
