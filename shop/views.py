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
    product=Product.objects.get(id=pk)
    favo=Favourites()
    favo.user=request.user
    favo.name=product.name
    favo.image=product.image
    favo.unit=product.selling_price
    favo.save()
    messages.success(request,"basarı ile kayıt olundu ")
    return redirect("home")
def favourite_page(request):
    favo=Favourites.objects.filter(user=request.user)
    return render(request,"shop/favorite_page.html",{"favos":favo})
def delete_favo(request,pk):
    Favourites.objects.get(id=pk).delete()
    return redirect("favourite")

def save_carts(request,pk):
    page_source=request.body
    soup=bs(page_source,"html.parser")
    num=soup.find("input",attrs={"name":"qty"})
    print(request)
    return redirect("home")
    
    product=Product.objects.get(id=pk)
    cart=Carts()
    cart.quantity=num
    cart.unit=product.selling_price
    cart.amount=num*cart.unit
    cart.user=request.user
    cart.name=product.name
    cart.image=product.image
    cart.save()
    messages.success(request,"basarı ile kayıt olundu ")
    












