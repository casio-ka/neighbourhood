from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Neighbourhood, Business, Post
from cloudinary.models import CloudinaryField

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'profile_picture']

class NeighbourHoodForm(forms.ModelForm):
    picture = CloudinaryField('image')

    class Meta:
        model = Neighbourhood
        fields = ('picture', 'name', 'location','health','police')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('name', 'email', 'description')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'post')