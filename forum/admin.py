from django.contrib import admin
from .models import Discussion, Category, AdvUser

# Register your models here.
admin.site.register(Discussion)
admin.site.register(Category)
admin.site.register(AdvUser)
