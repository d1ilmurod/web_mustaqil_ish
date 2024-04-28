from django.shortcuts import render
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
