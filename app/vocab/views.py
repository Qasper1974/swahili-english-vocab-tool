from unicodedata import name
from django.shortcuts import render

from .models import Vocabulary
# from sev import forms

# Create your views here.

def home(request):
    return render(request, 'home.html')

def ste(request):
    voc = Vocabulary.objects.order_by('swahili_word')
    context = {'voc' : voc}
    return render(request, 'swahili_to_english.html', context)

def create_word(request):
    # form = forms.VocabularyForm()
    # if request.method == 'POST':
    #     form = form.VocabularyForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         # return redirect('home.html')
    context = {}
    return render(request, 'vocab_form.html', context)