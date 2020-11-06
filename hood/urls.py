from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    index,
    register,
    profile,
    edit_profile,
    create_hood,
    allhoods,
    join_a_hood,
    leave_hood,
    hood,
    hoodpopulation,
    business,
    post,
    search,
)

urlpatterns=[
    path('',index,name = 'index'),
    path('register/', register, name='register'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('profile/<username>/', profile, name='profile'),
    path('profile/<username>/edit', edit_profile, name='edit'),
    path('create-a-hood/', create_hood, name='create_a_hood'),
    path('allhoods/', allhoods, name='allhoods'),
    path('hood/<hood_id>', hood, name='hood'),
    path('join-hood/<id>', join_a_hood, name='join'),
    path('leave-hood/<id>', leave_hood, name='leave'),
    path('population/<hood_id>', hoodpopulation, name='population'),
    path('business/<hood_id>', business, name='business'),
    path('post/<hood_id>', post, name='post'),
    path('search/', search, name='search_results'),
]