from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1, 'name':'Python'},
    {'id':2, 'name':'C++'},
    {'id':3, 'name':'Matplotlib'},
    {'id':4, 'name':'Pandas'},
]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'home.html', context)

def room(request):
    return render(request, 'room.html')
