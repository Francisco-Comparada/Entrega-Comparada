from django.contrib import admin
from sneakers.models import Jordans, Air_Force, Accessories

@admin.register(Jordans)
class Jordans_admin(admin.ModelAdmin):
    list_display = ['model', 'price', 'coulor','description','stock','img']

@admin.register(Air_Force)
class Air_Force_admin(admin.ModelAdmin):
    list_display = ['model', 'price', 'coulor','description','stock','img']

@admin.register(Accessories)
class Accessories_admin(admin.ModelAdmin):
    list_display = ['name', 'price','description','stock','img']
