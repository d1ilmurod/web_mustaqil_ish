from django.urls import path
from .views import index_page_view,contact_page,about_page,news_detail,galireya_view,shop_about_detail,ContactPageView


urlpatterns = [
    # path('',ProductAll.as_view(),name='products'),
    path('',index_page_view,name='index'),
    # path('contact',contact_page,name='contact'),
    path('contact/',ContactPageView.as_view(),name='contact'),
    path('about',about_page,name='about_shop'),
    path('shop-about/<int:pk>/',shop_about_detail,name='shop_about'),
    path("product/<int:pk>/", news_detail, name="post_detail"),
    path("products/", galireya_view, name="products"),
]

