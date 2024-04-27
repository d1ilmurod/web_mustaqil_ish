from django.contrib import admin
from .models import Products,Kinds
# Register your models here.

admin.site.register(Kinds)
admin.site.register(Products)