from django import views
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def ste(request):
    return render(request, 'home-copy.html')