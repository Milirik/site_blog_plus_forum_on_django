from django.contrib import admin
from .models import Post, Project, Feedback, Article, Tag, AboutPage

def short_content_for_admin_panel(obj):
	"""Выводит в админке сокращенный текст"""
	return f'{obj.content[:200]}....'
short_content_for_admin_panel.short_description = 'Текст(скоращенный)'


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', short_content_for_admin_panel, 'date_pub', 'image')
	search_fields = ('title', 'description', 'content')
	filter_horizontal = ('tags',)


class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', short_content_for_admin_panel, 'date_pub', 'image')
	search_fields = ('title', 'description', 'content')


class FeedbackAdmin(admin.ModelAdmin):
	list_display = ('name', 'body')  
	search_fields = ('name', 'body')
	readonly_fields = ('name', 'body')


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', short_content_for_admin_panel, 'date_pub')
	search_fields = ('title', 'description', 'content', 'date_pub')


class TagAdmin(admin.ModelAdmin):
	list_display = ('name', 'color')
	fiels = (('name', 'master'), ('color'))



admin.site.register(Post, PostAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(AboutPage)