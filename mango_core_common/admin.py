from django.contrib import admin
from django.contrib.admin import ModelAdmin

from mango_core_common.models import Animal


class AnimalModelAdmin(ModelAdmin):
    list_display = ('name', 'sound',)

admin.site.register(Animal, AnimalModelAdmin)
