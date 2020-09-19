from .models import Discussion

def forum_context_processor(request):
	context = {}
	if Discussion.objects.all():
		context['popular_discuss'] = Discussion.objects.order_by('rating').reverse()[0]
	context['user_rating'] = sum([dis.rating for dis in Discussion.objects.all()])
	return context