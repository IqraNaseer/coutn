from django.shortcuts import render
from .models import Contact,Client,Inquiry
from math import ceil
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def home(request):
    return render(request,'home.html')



def contact(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name,email=email, phone=phone, desc=desc)
        contact.save()
        message=request.POST['desc']
        em = request.POST['email']
        body = message + em
        send_mail("contact form",body,settings.EMAIL_HOST_USER,["raengineeringsolution@gmail.com"],fail_silently=False)
    return render(request,'contact.html')


def inquiry(request):
    if request.method=="POST":
        fname = request.POST.get('name', '')
        email = request.POST.get('email', '')
        title = request.POST.get('title', '')
        company = request.POST.get('company', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('code', '')
        phone = request.POST.get('phone', '')
        inq = Inquiry( name = fname,email=email,title=title,company=company, address=address, city=city,state=state, zip_code=zip_code, phone=phone)
        inq.save()
        message=request.POST['name']
        tie = request.POST['title']
        em = request.POST['email']
        com = request.POST['company']
        body = message + " " + em + " " + com +" " + tie
        send_mail("contact form",body,settings.EMAIL_HOST_USER,["raengineeringsolution@gmail.com"],fail_silently=False)
    return render(request, 'inquiry.html')

def about(request):
    return render(request,'about.html')

def clients(request):
    clint = Client.objects.all()
    n = len(clint)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': clint}
    return render(request, 'clients.html',params)


def services_ov(request):
    return render(request,'services_overview.html')


def calibration(request):
    return render(request,'calibratn.html')

def verify(request):
    return render(request,'verification.html')

def product(request):
    return render(request,'prod.html')