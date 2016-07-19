from django.contrib import admin
from django.contrib.admin import ModelAdmin

from src.models import Animal


class AnimalModelAdmin(ModelAdmin):
    list_display = ('name', 'sound',)

admin.site.register(Animal, AnimalModelAdmin)
