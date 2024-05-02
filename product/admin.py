from django.contrib import admin
from .models import Products,Kinds,AboutCandyShop,Contact,AboutMe
# Register your models here.

admin.site.register(Kinds)
admin.site.register(Products)
admin.site.register(AboutCandyShop)
admin.site.register(Contact)
admin.site.register(AboutMe)

