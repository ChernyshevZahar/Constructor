from django.contrib import admin
from .models import Bot

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'token')

admin.site.register(Bot, MyModelAdmin)
