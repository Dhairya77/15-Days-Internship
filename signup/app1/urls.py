from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('',views.sign,name="signup"),
    path('verify',views.verify,name="verify"),
]
