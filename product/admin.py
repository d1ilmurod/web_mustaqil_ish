from django.contrib import admin
from .models import Products,Kinds,AboutCandyShop
# Register your models here.

admin.site.register(Kinds)
admin.site.register(Products)
admin.site.register(AboutCandyShop)

