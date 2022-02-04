from unicodedata import name
from django.shortcuts import render

from .models import Vocabulary
# Create your views here.

def home(request):
    return render(request, 'home.html')

def ste(request):
    voc = Vocabulary.objects.order_by('swahili_word')
    context = {'voc' : voc}
    return render(request, 'swahili_to_english.html', context)