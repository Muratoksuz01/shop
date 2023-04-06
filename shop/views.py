from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from bs4 import BeautifulSoup as bs
from .models import *
from .forms import RegisterForm
# Create your views here.

def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success (request, f"Account Created for {username}")
            return redirect("login")
    else:
        form=RegisterForm()
    context={"form":form}
    return render(request,"shop/register.html",context)

def home(request):
    products=Product.objects.all()
    context={"products":products}
    return render(request,"shop/index.html",context)
def product_detail(request,slug):
    product=Product.objects.get(slug=slug)
    return render(request,"shop/product_detail.html",{"product":product})

def save_favourites(request,pk):
    if request.user.is_authenticated:
        product=Product.objects.get(id=pk)
        favo=Favourites()
        favo.user=request.user
        favo.name=product.name
        favo.image=product.image
        favo.unit=product.selling_price
        favo.save()
        messages.success(request,"basarı ile kayıt olundu ")
        return redirect("home")
    else:
        messages.warning(request,"please login")
        return redirect("login")

def favourite_page(request):
    if request.user.is_authenticated:
        favo=Favourites.objects.filter(user=request.user)
        return render(request,"shop/favorite_page.html",{"favos":favo})
    else:
        messages.warning(request,"please login")
        return redirect("login")
def delete_favo(request,pk):
    Favourites.objects.get(id=pk).delete()
    return redirect("favourite")

def save_carts(request, input_value, product_id):
    product = Product.objects.get(id=product_id)
    cart = Carts()
    cart.quantity = input_value
    cart.unit = product.selling_price
    cart.amount = input_value * cart.unit
    cart.user = request.user
    cart.name = product.name
    cart.image = product.image
    cart.save()
    messages.success(request, "Başarı ile kaydedildi.")
    return redirect("home")
    
def collection(request):
    collect=Catagorys.objects.all()
    return render(request,  "shop/collections.html",{"collects":collect})

def collection_detail(request,pk):
    category = Catagorys.objects.get(id=pk)
    products = Product.objects.filter(categories=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request,"shop/collection_detail.html",context=context)









