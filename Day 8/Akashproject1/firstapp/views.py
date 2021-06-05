from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request,'Home.html')

def aboutpage(request):
    return render(request,'About.html')

def contactpage(request):
    return render(request,'Contact.html')