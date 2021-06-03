from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("<h1>Welcome to the world of <strong>django</strong></h1>")

def aboutpage(request):
    return HttpResponse("<h1>About</h1><br>I am a python developer and eager to work with it")

def contactpage(request):
    return HttpResponse("<h1>CONTACT</h1><br>You can contact me through mail at abc@xyz.com")