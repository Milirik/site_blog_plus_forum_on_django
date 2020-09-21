from django import template

from forum.models import ForumLikes

register = template.Library()


@register.simple_tag(takes_context=True)
def is_liked(context, discussion_id):
	request = context['request']
	try:
		forum_likes = ForumLikes.objects.get(discussion__pk = discussion_id, liked_by = request.user.pk).like
	except Exception as e:
		forum_likes = False

	return forum_likes


@register.simple_tag()
def count_likes(discussion_id):
	return ForumLikes.objects.filter(discussion__pk = discussion_id, like=True).count()


@register.simple_tag()
def top_likes(user_id):
	return ForumLikes.objects.filter(discussion__pk = discussion_id, like=True).count()



@register.simple_tag(takes_context=True)
def forum_likes_id(context, discussion_id):
	request = context['request']
	return ForumLikes.objects.get(discussion__pk = discussion_id, liked_by=request.user.pk).pk