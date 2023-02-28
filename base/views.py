from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm, UserForm
from django.contrib.auth.models import User

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
    queryTopic = request.GET.get('queryTopic') if request.GET.get('queryTopic') != None else ''
    rooms = Room.objects.filter(topic__name__icontains=queryTopic)

    topics = Topic.objects.all()

    context = {'rooms':rooms,
               'topics':topics}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid:
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    context = {'obj': room}
    return render(request, 'base/delete.html', context)

def addUser(request):

    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid and request.POST.get('username') and request.POST.get('password'):
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/add_user.html', context)

def deleteUser(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid:
            name = request.POST.get('username')
            passw = request.POST.get('password')
            #TODO it works only with existing user
            user = User.objects.get(username=name, password=passw)
            user.delete()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/delete_user.html', context)