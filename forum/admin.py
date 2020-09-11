from django.contrib import admin
import datetime
from .models import Discussion, Category, AdvUser, Answer
from .utilities import send_activation_notification


def send_activation_notifications(modeladmin, request, queryset):
	for rec in queryset:
		if not rec.is_activated:
			send_activation_notification(rec)
	modeladmin.message_user(request, 'Письма с оповещениями отправлены')

send_activation_notifications.short_description = 'Отправка писем с оповещениями об активации'


class NonactivatedFilter(admin.SimpleListFilter):
	title = 'Прошли активацию?'
	parameter_name = 'actstate'

	def lookups(self, request, model_admin):
		return(
			('activated', 'Прошли'),
			('threedays', 'Не прошли более 3 дней'),
			('week', 'Не прошли более недели'), 
			)
	

class AdvUserAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'is_activated', 'date_joined')
	se




# Register your models here.
admin.site.register(AdvUser)
admin.site.register(Category)
admin.site.register(Discussion)
admin.site.register(Answer)