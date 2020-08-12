from django.shortcuts import render
from .models import Discussion, Category

# Create your views here.
def index(request):
	categories = Category.objects.all()
	discussions = Discussion.objects.all()
	return render(request, 'forum/index.html', 
		context={
		'categories':categories,
		'discussions':discussions,
		})