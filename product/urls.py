from django.urls import path
from .views import index_page_view


urlpatterns = [
    # path('',ProductAll.as_view(),name='products'),
    path('',index_page_view,name='products'),
]
