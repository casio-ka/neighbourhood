from django.shortcuts import render, redirect, get_object_or_404
from django.http  import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm,UpdateUserForm,UpdateProfileForm,NeighbourHoodForm,BusinessForm, PostForm
from .models import Profile, User, Neighbourhood, Business, Post


# Create your views here.

def index(request):
     return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')


            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form}) 



def profile(request, username):
    return render(request, 'profile.html')


