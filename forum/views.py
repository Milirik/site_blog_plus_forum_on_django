from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Discussion, Category

# Pages
def index(request):
	categories = Category.objects.all()
	discussions = Discussion.objects.all()
	return render(request, 'forum/index.html', 
		context={
		'categories':categories,
		'discussions':discussions,
		})

# User
class ForumLoginView(LoginView):
	template_name = 'forum/login.html'


class ForumLogoutView(LoginRequiredMixin, LogoutView):
	template_name = 'forum/logout.html'


@login_required
def profile(request):
	return render(request, 'forum/profile.html')
	