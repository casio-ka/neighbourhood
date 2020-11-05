from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns=[
    path('',views.index,name = 'index'),
    path('register/', views.register, name='register'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('profile/<username>/', views.profile, name='profile'),

]