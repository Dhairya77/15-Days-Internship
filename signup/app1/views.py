from django.shortcuts import render
from django.urls import path
# Create your views here.
def sign(request):
    return render(request,'signupform.html')

def verify(request):
    f = request.POST['fname']
    l = request.POST['lname']
    m = request.POST['mail']
    p = request.POST['password']
    return render(request,'verify.html',{'fname':f,'lname':l,'mail':m,'ps':p})