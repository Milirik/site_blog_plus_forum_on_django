from django.db import models
from datetime import datetime  #.utilities
from os.path import splitext #.utilities
from ckeditor.fields import RichTextField

def get_timestamp_path(instance, filename):
	return '%s%s' % (datetime.now().timestamp(), splitext(filename)[1])

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100, db_index=True, verbose_name='Название поста')
	description = models.TextField(max_length=2000,blank=True, verbose_name='Краткое описание поста')
	content = RichTextField(max_length=2000, verbose_name='Текст поста')
	date_pub = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации поста')
	image = models.ImageField(blank=True, upload_to=get_timestamp_path,  verbose_name='Изображение') 
	tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

	def __str__(self):
		return f'{self.title}'


	class Meta:
		verbose_name='Пост'
		verbose_name_plural='Посты'
		ordering = ['-date_pub']


class Project(models.Model):
	title = models.CharField(max_length=30, db_index=True, verbose_name='Название проекта')
	description = models.TextField(max_length=180,blank=True, verbose_name='Краткое описание проекта')
	content =RichTextField(blank=True, db_index=True, verbose_name='Описание проекта')
	date_pub = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации проекта')
	image = models.ImageField(blank=True, null=True, upload_to=get_timestamp_path, verbose_name='Изображение')
 	 

	def __str__(self):
		return f'{self.title}'


	class Meta:
		verbose_name='Проект'
		verbose_name_plural='Проекты'
		ordering = ['-date_pub']
		

class Feedback(models.Model):
	name = models.CharField(max_length=150, db_index=True, verbose_name='Ваше имя', help_text="<span style='font-style:italic;'>Обязательно к заполнению</span>")
	body = models.TextField(blank=False, db_index=True, verbose_name='Текст письма', help_text="<span style='font-style:italic;'>Обязательно к заполнению</span>")

	def __str__(self):
		return f'{self.name}'

	class Meta:
		verbose_name='Фидбек'
		verbose_name_plural='Отзывы'
	
		
class Article(models.Model):
	title = models.CharField(max_length=150, db_index=True, verbose_name='Название статьи')
	description = models.TextField(max_length=2000, db_index=True, verbose_name='Краткое описание статьи')
	content = RichTextField(blank=True, db_index=True, verbose_name='Текст статьи')
	date_pub = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

	def __str__(self):
		return f'{self.title}'

	class Meta:
		verbose_name='Статья'
		verbose_name_plural='Статьи'
		ordering = ['-date_pub']

class Tag(models.Model):
	colors = (
		('RED', 'red'),
		('DEFAULT', '#3ba2b9'),
		('YELLOW', 'yellow'),
		('GREEN', 'green'),
		('GRAY', 'gray')
		)
	
	name = models.CharField(max_length=30, db_index=True, verbose_name='Название тэга')
	color = models.CharField(max_length=30, db_index=True, choices=colors, default='#3ba2b9', verbose_name='Цвет тэга')

	def __str__(self):
		return f'{self.name}'

	class Meta:
		verbose_name='Тэг'
		verbose_name_plural = 'Тэги'

class AboutPage(models.Model):
	name = models.CharField(max_length=150, verbose_name='Имя')
	age = models.CharField(max_length=150, verbose_name='Возраст')
	technology_stack = models.TextField(blank=True, verbose_name='Стэк технологий')
	image = models.ImageField(blank=True, null=True, upload_to=get_timestamp_path, verbose_name='Изображение')
	info = RichTextField(blank=True, verbose_name='Дополнительная информация')

	def __str__(self):
		return f'{self.name}'

	class Meta:
		verbose_name='Про меня'

