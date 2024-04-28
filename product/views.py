from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
# Create your views here.
from .models import Products

# class ProductAll(ListView):
#     model = Products
#     template_name = 'list.html'
#     context_object_name = 'alls'


def index_page_view(request):
    data = Products.objects.all()

    context = {
        'data': data,
    }


    return render(request,'index.html',context)


def contact_page(request):

    return render(request,'contact.html')


def about_page(request):

    return render(request,'contact.html')


def news_detail(request, pk):
    template_name = 'about.html'
    post = Products.objects.get(pk=pk)
    context = {
        'post': post
    }

    return render(request, template_name=template_name, context=context)



