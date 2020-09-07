from django.contrib import admin
from .models import Discussion, Category, AdvUser, Answer

# Register your models here.
admin.site.register(AdvUser)
admin.site.register(Category)
admin.site.register(Discussion)
admin.site.register(Answer)