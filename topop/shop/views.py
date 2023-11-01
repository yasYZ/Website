from django.shortcuts import render, HttpResponse
from .models import Product
# Create your views here.


def products(request):
    all_products = Product.objects.all()
    return render(request, 'En/Codeshop.html', {'products': all_products})
