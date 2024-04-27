from django.urls import path
from .views import ProductAll


urlpatterns = [
    path('',ProductAll.as_view(),name='products')
]
