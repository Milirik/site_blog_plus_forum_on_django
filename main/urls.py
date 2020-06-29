from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = 'main'

urlpatterns = [
    path('', index, name='index_name'),
    path('with_tag/<int:id_tag>', by_tag, name='by_tag_name'),
    path('forum/', include('forum.urls', namespace='')),
    path('projects/', projects, name='projects_name'),
    path('articles/', articles, name='articles_name'),
    path('about/', about, name='about_name'),
    path('contacts/', contacts, name='contacts_name'),

    path('project/detail/<int:pk>/', project_detail, name='project_detail_name'),
    path('article/detail/<int:pk>/', article_detail, name='article_detail_name'),
] 

