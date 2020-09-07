from django.db import models

from django.dispatch import Signal

from django.contrib.auth.models import AbstractUser

from .utilities import get_timestamp_path, send_activation_notification

import random


# Users
user_registrated = Signal(providing_args=['instance'])

def user_registerated_dispatcher(sender, **kwargs):
	send_activation_notification(kwargs['instance'])

user_registrated.connect(user_registerated_dispatcher)


class AdvUser(AbstractUser):
	is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошел активацию?')
	send_messages = models.BooleanField(default=True, verbose_name='Слать оповещения о новых комментариях?')
	image = models.ImageField(blank=True, default=f'cats/cat{random.randint(1,3)}.jpg', upload_to=get_timestamp_path, verbose_name='Изображение')

	class Meta(AbstractUser.Meta):
		pass



# Content
class Category(models.Model):
	name = models.CharField(max_length=30, db_index=True, unique=True, verbose_name='Название категории')
	
	def __str__(self):
		return f'Категория "{self.name}"'

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'


class Discussion(models.Model):
	text = models.TextField(max_length=200, db_index=True, verbose_name='Текст обсуждения')
	category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT, null=False)
	creator = models.ForeignKey(AdvUser, verbose_name='Создатель', on_delete=models.CASCADE, null=True)
	date_of_creation = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')
	rating = models.IntegerField(default=0, verbose_name='Рейтинг')

	def __str__(self):
		return f'Обсуждение "{self.text[:10 if len(self.text)>10 else -1]}.."'

	class Meta:
		verbose_name = 'Обсуждение'
		verbose_name_plural = 'Обсуждения'


class Answer(models.Model):
	text = models.TextField(max_length=200, db_index=True, verbose_name='Текст ответа')
	discussion = models.ForeignKey(Discussion, verbose_name='Обсуждение', on_delete=models.CASCADE, null=True)
	creator = models.ForeignKey(AdvUser, verbose_name='Создатель', on_delete=models.CASCADE, null=True)
	date_of_creation = models.DateField(auto_now_add=True, db_index=True, verbose_name='Создано')

	def __str__(self):
		return f'Ответ {self.creator.username} - {self.text[:10 if len(self.text)>10 else -1]}....'

	class Meta:
		verbose_name='Комментарий'
		verbose_name_plural = 'Комментарии'
		ordering = ['-date_of_creation']