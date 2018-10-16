from django.shortcuts import render
from django.views.generic import Loginscreen

def home(request):
    return render(request, 'login.html')
