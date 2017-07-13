from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Treasure
from .forms import TreasureForm, LoginForm

# Create your views here.

def index( request):
    name    = 'Gold Nugget'
    value   = 1000.00
    treasures = Treasure.objects.all
    form = TreasureForm()
    return render( request, 'index.html', {'treasures': treasures, 'form': form}) 

def detail( request, treasure_id):
    treasure = Treasure.objects.get( id = treasure_id)
    return render( request, 'detail.html', {'treasure': treasure})
 
def post_treasure( request):
    form = TreasureForm( request.POST, request.FILES)
    if form.is_valid():
        treasure = form.save( commit = False)
        treasure.user = request.user
        treasure.save()
    return HttpResponseRedirect( '/')

def profile( request, username):
    user = User.objects.get(username = username)
    treasures = Treasure.objects.filter(user=user)
    return render( request, 'profile.html', {
        'username' : username,
        'treasures' : treasures,
    })

def login_view( request):
    if request.method == 'POST':    
        form = LoginForm( request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate( username = u, password = p)
            if user is not None:
                if user.is_active:
                    login( request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account is not active")
            else:
                print("Username and password don't match")
    else :
        form = LoginForm()
        return render( request, 'login.html', {'form': form})
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = UserCreationForm()
        return render( request, 'registration.html', {'form': form})

