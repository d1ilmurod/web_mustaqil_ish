from django.urls import path
from .views import index_page_view,contact_page,about_page,news_detail


urlpatterns = [
    # path('',ProductAll.as_view(),name='products'),
    path('',index_page_view,name='products'),
    path('contact',contact_page,name='contact'),
    path('about',about_page,name='about'),
    path("detail/<int:pk>/", news_detail, name="post_detail")
]
