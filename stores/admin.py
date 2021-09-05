from django.contrib import admin

from .models import FoodStore , Item

# Register your models here.

admin.site.register(FoodStore)
admin.site.register(Item)