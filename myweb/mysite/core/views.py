from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import product,Contact,Orders,Booking,select,measurement
from math import ceil
from .forms import *
from django.conf import settings # new
from django.views.generic.base import TemplateView


def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'

def prodt(request):
    prod = product.objects.all()
    n = len(prod)
    nSlides = n//4 + ceil((n/4)-(n//4))
    if User.is_authenticated:
        condition = True
    else:
        condition = False
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': prod,'condition': condition}
    return render(request, 'home.html',params)



def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'contact.html')


def Request(request):
    return render(request, 'wants.html')

def price(request):
    return render(request, 'trend.html')

def productView(request, myid):
    # Fetch the product using the id
    Product = product.objects.filter(id=myid)
    return render(request, 'product.html', {'product':Product[0]})

def check(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        Quantity = request.POST.get('quantity', '')
        Delivery = request.POST.get('Delivery', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone,clothes_detail=Delivery,quantity=Quantity)
        order.save()
        
        return render(request, 'checkout.html')
    return render(request, 'checkout.html')

def book(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        Quantity = request.POST.get('quantity', '')
        Delivery = request.POST.get('Delivery', '')
        phone = request.POST.get('phone', '')
        check = Booking(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone,clothes_detail=Delivery,quantity=Quantity)
        check.save()
        thank = True
        return render(request, 'order.html',{'thank':thank})
    return render(request, 'order.html')

def detail(request):
    if request.method=="POST":
        length = request.POST.get('lenght', '')
        seleves = request.POST.get('seleves', '')
        chest = request.POST.get('chest', '')
        west = request.POST.get('west', '')
        heap = request.POST.get('heap', '')
        shoulder = request.POST.get('shoulder', '')
        decs = request.POST.get('decs','')
        measure = measurement(fulllength = length,seleves = seleves,chest=chest,west=west,heap=heap,shoulder= shoulder,description=decs)
        measure.save()
    return render(request, 'detail.html')


def select(request):
    if request.method == 'POST': 
        form = selectForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save() 
            return render(request, 'select.html', {'form' : form})
    else: 
        form = selectForm() 
    return render(request, 'select.html', {'form' : form}) 
  
   # return render(request, 'select.html')


def checoutView(request):
    return render(request,'home1.html')
    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


