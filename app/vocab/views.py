from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Vocabulary
# Create your views here.

def home(request):
    return render(request, 'home.html')

def ste(request):
    voc = Vocabulary.objects.all()
    context = {'voc' : voc}
    return render(request, 'swahili_to_english.html', context)