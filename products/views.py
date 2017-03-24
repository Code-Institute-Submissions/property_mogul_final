from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@login_required(login_url='/login/')
def all_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products})
