from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,TemplateView
from .forms import ContactForm
from .models import Products,AboutCandyShop,AboutMe

# class ProductAll(ListView):
#     model = Products
#     template_name = 'list.html'
#     context_object_name = 'alls'


def index_page_view(request):
    data = Products.objects.all()
    datas = AboutCandyShop.objects.all()
    about_me = AboutMe.objects.all()


    context = {
        'data': data,
        'datas': datas,
        'about_me': about_me,
    }


    return render(request,'index.html',context)


def contact_page(request):

    return render(request,'contact.html')


def about_page(request):
    template_name = 'about.html'
    about_shop = AboutCandyShop.objects.all()

    context = {
        'about_shop': about_shop,
    }


    return render(request,'about.html',context)


def news_detail(request, pk):
    template_name = 'detail.html'
    post = Products.objects.get(pk=pk)
    context = {
        'post': post
    }

    return render(request, template_name=template_name, context=context)



def shop_about_detail(request, pk):
    template_name = 'shop_about_detail.html'
    one = AboutCandyShop.objects.get(pk=pk)
    context = {
        'one': one,
    }

    return render(request, template_name=template_name, context=context)




def galireya_view(request):
    products = Products.objects.all()

    context = {
        'products':products,
    }

    return render(request,'gallery.html',context)





class ContactPageView(TemplateView):
    templates_name = 'contact.html'
    def get(self,request,*args,**kwargs):
        form = ContactForm()

        context = {
            'form': form,
        }

        return render(request,"contact.html",context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)

        if request.method == 'POST':
            form.save()
            return HttpResponse("<h1>Xabaringiz yuborildi</h1>")

        context = {
            'form': form
        }

        return render(request, "contact.html", context)








