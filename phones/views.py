from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', '')
    if sort == 'name':
        phones = Phone.objects.order_by('name')
        context = {'phones': phones}
        return render(request, template, context)

    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price')
        context = {'phones': phones}
        return render(request, template, context)

    elif sort == 'min_price':
        phones = Phone.objects.order_by('price')
        context = {'phones': phones}
        return render(request, template, context)

    context = {'phones': Phone.objects.all()}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.get(slug=slug)
    context = {'phone': phones}
    return render(request, template, context)
