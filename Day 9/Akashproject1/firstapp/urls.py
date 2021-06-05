from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name="HOME"),
    path('about',views.aboutpage,name="ABOUT"),
    path('contact',views.contactpage,name="CONTACT"),
    path('form',views.formpage,name="FORM"),
    path('formprocess',views.formprocess,name="FP")
]