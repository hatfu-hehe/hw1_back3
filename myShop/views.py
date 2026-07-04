from django.shortcuts import render

from . import models

def cart_view(request):
    if request.method == 'GET':
        products = models.Product.objects.all()
        context = {'products': products}
    return render(request, template_name='products.html', context=context)

def categ_view(request):
    if request.method == 'GET':
        categories = models.Category.objects.all()
        context = {'categories': categories}
    return render(request, template_name='categories.html', context=context)