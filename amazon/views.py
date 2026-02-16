from django.shortcuts import render,redirect
from .models import Product
# Create your views here.

def product_list(request):
    products=Product.objects.all()
    return render (request,'store/product_list.html',{'products':products})

def product_details(request,id):
    product = Product.objects.get(id=id)
    return render(request,'store/product_details.html',{'product':product})

def add_to_cart(request,id):
    cart=Product.session.get('cart',{})
    cart[id]=cart.get(id,0)+1
    request.session['cart']=cart
    return redirect('product_list')

def view_cart(request):
    cart=request.session.get('cart',{})
    products= Product.objects.filter(id__in=cart.keys())
    return render(request,'store/cart.html',{'products':products,'cart':cart})