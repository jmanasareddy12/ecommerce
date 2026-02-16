from django.shortcuts import render
from .models import Product
# Create your views here.

def product_list(request):
    products=Product.objects.all()
    return render (request,'store/product_list.html',{'products':products})

def product_details(request,id):
    product = Product.objects.get(id=id)
    return render(request,'store/product_details.html',{'product':product})