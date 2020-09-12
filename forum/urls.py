from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = 'forum'

urlpatterns = [
	path('discuss/<int:pk>/', detail, name = "detail_discuss_name"),

	path('register/activate/<str:sign>/', user_activate, name='register_activate_name'),
	path('register/done/', RegisterUserDoneView.as_view(), name='register_done_name'),
	path('register/', RegisterUserView.as_view(), name='register_name'),

	path('profile/add/', profile_add_discuss, name='profile_add_discuss_name'),
	path('profile/delete/<int:pk>/', profile_delete_discuss, name='profile_delete_discuss_name'),
	path('profile/change/', ChangeUserInfoView.as_view(), name='profile_change_name'),
	path('profile/delete/', DeleteUserView.as_view(), name='profile_delete_name'),
	path('profile/', profile, name='profile_name'),

	path('password/change/', ForumPasswordChangeView.as_view(), name='password_change_name'),
	path('logout/', ForumLogoutView.as_view(), name='logout_name'),
	path('login/', ForumLoginView.as_view(), name='login_name'),
	

    path('', index, name='index_name'),

] 

