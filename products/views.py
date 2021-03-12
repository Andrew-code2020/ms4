from django.shortcuts import render
from .models import Product
# Create your views here.

def all_products(request):
    """function to render classes and membership page"""
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
