from .models import Discussion

def forum_context_processor(request):
	context = {}
	context['popular_discuss'] = Discussion.objects.order_by('rating').reverse()[0]
	return context