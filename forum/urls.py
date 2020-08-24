from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = 'forum'

urlpatterns = [
	path('logout/', ForumLogoutView.as_view(), name='logout_name'),
	path('login/', ForumLoginView.as_view(), name='login_name'),
	path('profile/', profile, name='profile_name'),
    path('', index, name='index_name'),

] 

