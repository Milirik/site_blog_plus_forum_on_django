from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages

from django.core.paginator import Paginator

from django.db.models import Q

import random

from .models import Post, Project, Feedback, Article, Tag, AboutPage
from .forms import FeedbackForm, SearchForm

#Pages
def index(request):                     
	if request.method == 'POST':
		contacts(request=request)

	posts = Post.objects.all()        	
	form_contact = FeedbackForm()                 
	rnd_article = Article.objects.get(pk=random.randint(1, Article.objects.count()))

	paginator = Paginator(posts, 3)
	page_number = request.GET.get('page', default=1)
	page = paginator.get_page(page_number)
	is_paginated = page.has_other_pages()
	prev_url = '?page={}'.format(page.previous_page_number()) if page.has_previous() else ''
	next_url = '?page={}'.format(page.next_page_number()) if page.has_next() else ''

	context = {'page_object': page,
			 'is_paginated': is_paginated,
			 'next_url':next_url,
			 'prev_url':prev_url,
		     'page': page,
		     'rnd_article':rnd_article,
		     'form_contact': form_contact,
		     }
	context['posts'] = posts
	return render(request, 'main/index.html', context)

def by_tag(request, id_tag):
	if request.method == 'POST':
		contacts(request=request)
	posts = Tag.objects.filter(pk=id_tag).first().posts.all() 
	form_contact = FeedbackForm()                 
	rnd_article = Article.objects.get(pk=random.randint(1, Article.objects.count()))

	paginator = Paginator(posts, 3)
	page_number = request.GET.get('page', default=1)
	page = paginator.get_page(page_number)
	is_paginated = page.has_other_pages()
	prev_url = '?page={}'.format(page.previous_page_number()) if page.has_previous() else ''
	next_url = '?page={}'.format(page.next_page_number()) if page.has_next() else ''

	context = {'page_object': page,
			 'is_paginated': is_paginated,
			 'next_url':next_url,
			 'prev_url':prev_url,
		     'page': page,
		     'rnd_article':rnd_article,
		     'form_contact': form_contact,
		     }
	context['posts'] = posts
	context['tag_'] = Tag.objects.filter(pk=id_tag).first()
	return render(request, 'main/by_tag.html', context)

def projects(request):
	projects = Project.objects.all()
	return render(request, 'main/projects_page.html', context={'projects': projects})

def articles(request):
	if 'search' in request.GET:
		search = request.GET['search']
		articles = Article.objects.filter(Q(title__icontains=search)|Q(content__icontains=search))
	else:
		articles = Article.objects.all()

	form = SearchForm()
	paginator = Paginator(articles, 5)
	page_number = request.GET.get('page', default=1)
	page = paginator.get_page(page_number)
	is_paginated = page.has_other_pages()
	prev_url = '?page={}'.format(page.previous_page_number()) if page.has_previous() else ''
	next_url = '?page={}'.format(page.next_page_number()) if page.has_next() else ''

	context={'page_object': page,
			 'is_paginated': is_paginated,
			 'next_url':next_url,
			 'prev_url':prev_url,
			 'articles': articles,
		     'page': page,
		     'form': form,
		     }

	return render(request, 'main/articles_page.html', context)

def about(request):
	me = AboutPage.objects.first()
	return render(request, 'main/about_page.html', context={'me':me})

def contacts(request):
	form = FeedbackForm()
	if request.method == 'GET':
		return render(request, 'main/contacts_page.html', context={'form':form})
	else:
		form_new = FeedbackForm(request.POST)
		if form_new.is_valid():
			form_new.save()
			messages.add_message(request, messages.SUCCESS, 'Успешно отправлено')
		else:
			messages.add_message(request, messages.ERROR, 'Captcha введена не правильно')
			return render(request, 'main/contacts_page.html', context={'form':form_new})
		return render(request, 'main/contacts_page.html', context={'form':form})

def other_page(request, page):
	try:
		template = get_template('main/' + page + '.html')
	except TemplateDoesNotExist:
		raise Http404
	return HttpResponse(template.render(request=request))


#Detail objects
def project_detail(request, pk):
	project = get_object_or_404(Project, pk=pk)
	context = {'project': project}
	return render(request, 'main/project_detail.html', context)

def article_detail(request, pk):
	article = get_object_or_404(Article, pk=pk)
	context = {'article': article}
	return render(request, 'main/article_detail.html', context)


#Errors
def my_custom_page_not_found_view(request, exception):
	return render(request, 'main/404.html', context={})
