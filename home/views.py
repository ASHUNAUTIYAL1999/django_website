from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


def index(request):
    return render(request,'index.html')
def about(request):
    return HttpResponse("this is about page")
def Contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        return render(request,'contact.html',{'message':'your message has been sent sucessfully '})
    return render(request,'contact.html')
def Services(request):
    return render(request,'Services.html')
def Email(request):
    return HttpResponse("Agarwal@gmail.com")
def Address(request):
    return HttpResponse("agarwal Group near railway station in front of SBI")
def Features(request):
    return render(request,'Features.html')
def Pricing(request):
    return render(request,'Pricing.html')
def Home(request):
    return render(request,'Home.html')
def ContactNo(request):
    return HttpResponse("8239051361")