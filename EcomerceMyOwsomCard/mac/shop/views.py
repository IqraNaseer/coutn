from django.shortcuts import render,redirect
from .models import product,Contact,Orders,bookrequest,loginform
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UsernameField
from django.contrib.auth.forms import UserModel
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from math import ceil

# Create your views here.

def index(request):
    allProds = []
    catprods = product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def Request(request):
    if request.method=="POST":
         name = request.POST.get('name', '')
         email = request.POST.get('email', '')
         phone = request.POST.get('phone', '')
         bookName = request.POST.get('bookName', '')
         BookRequest = bookrequest(name=name, email=email, phone=phone, bookN=bookName)
         BookRequest.save()
    return render(request, 'shop/request.html')



def search(request):
    return render(request,'shop/search.html')

def productView(request, myid):
    # Fetch the product using the id
    Product = product.objects.filter(id=myid)
    return render(request, 'shop/product.html', {'product':Product[0]})

def check(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    return render(request, 'shop/checkout.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'shop/account.html', {
        'form': form
    })

def login(request):
    return render(request,'shop/LogIn.html')


