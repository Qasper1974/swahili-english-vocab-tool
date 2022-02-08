from unicodedata import name
from django.shortcuts import render

from .models import Vocabulary
from .forms import VocabularyForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def ste(request):
    voc = Vocabulary.objects.order_by('swahili_word')
    context = {'voc' : voc}
    return render(request, 'swahili_to_english.html', context)

def ets(request):
    voc = Vocabulary.objects.order_by('english_translation')
    context = {'voc' : voc}
    return render(request, 'english_to_swahili.html', context)

def create_word(request):
    form = VocabularyForm()
    if request.method == 'POST':
        form = VocabularyForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('home.html')
    context = { 'form' : form}
    return render(request, 'vocab_form.html', context)