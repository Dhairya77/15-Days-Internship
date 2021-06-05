from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request,'Home.html')

def aboutpage(request):
    return render(request,'About.html')

def contactpage(request):
    return render(request,'Contact.html')

def formpage(request):
    return render(request,'form.html')

def formprocess(request):
    print(request.method)
    print(request.POST)
    a = int(request.POST['no1'])
    b = int(request.POST['no2'])
    c=a+b
    return render(request,'formprocess.html',{'mysum':c,'mya':a,'myb':b})