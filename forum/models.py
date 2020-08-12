from django.db import models
from django.contrib.auth.models import AbstractUser


# Users
class AdvUser(AbstractUser):
	is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошел активацию?')
	send_messages = models.BooleanField(default=True, verbose_name='Слать оповещения о новых комментариях?')
	text = models.CharField(max_length=20, default='Привет')

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
	title = models.TextField(max_length=200, db_index=True, verbose_name='Обсуждение')
	category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT, null=False)

	def __str__(self):
		return f'Обсуждение "{self.title[:10]}.."'

	class Meta:
		verbose_name = 'Обсуждение'
		verbose_name_plural = 'Обсуждения'
