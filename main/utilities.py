
from django.core.paginator import Paginator

import random

from .models import *
from .forms import *

def generations_for_main_page(request, posts):
	if request.method == 'POST' and id_tag:
		contacts(request=request)

	form_contact = FeedbackForm()                 
	rnd_article = Article.objects.get(pk=random.randint(1, Article.objects.count()))

	paginator = Paginator(posts, 3)
	page_number = request.GET.get('page', default=1)
	page = paginator.get_page(page_number)
	is_paginated = page.has_other_pages()
	prev_url = '?page={}'.format(page.previous_page_number()) if page.has_previous() else ''
	next_url = '?page={}'.format(page.next_page_number()) if page.has_next() else ''

	return {'page_object': page,
			 'is_paginated': is_paginated,
			 'next_url':next_url,
			 'prev_url':prev_url,
		     'page': page,
		     'rnd_article':rnd_article,
		     'form_contact': form_contact,
		     }