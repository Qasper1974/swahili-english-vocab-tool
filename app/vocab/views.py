from unicodedata import name
from django.shortcuts import render, redirect

from .models import Vocabulary
from .forms import VocabularyForm
from .filters import WordFilter

# Create your views here.

def home(request):
    return render(request, 'home.html')

def ste(request):
    voc = Vocabulary.objects.order_by('swahili_word')
    filter = WordFilter(request.GET, queryset=Vocabulary.objects.all())
    voc = filter.qs.order_by('swahili_word')
    display = False
    btntofilter = True
    context = {'voc' : voc, 'filter': filter, 'display' : display, 'btntofilter' : btntofilter}
    return render(request, 'swahili_to_english.html', context)

def stesort(request):
    voc = Vocabulary.objects.order_by('swahili_word')
    filter = WordFilter(request.GET, queryset=Vocabulary.objects.all())
    voc = filter.qs.order_by('swahili_word')
    display = True
    btntofilter = False
    filterpage = 'ste'
    context = {'voc' : voc, 'filter': filter, 'display' : display, 'btntofilter' : btntofilter, 'filterpage' : filterpage}
    return render(request, 'swahili_to_english.html', context)

def ets(request):
    voc = Vocabulary.objects.order_by('english_translation')
    filter = WordFilter(request.GET, queryset=Vocabulary.objects.all())
    voc = filter.qs.order_by('english_translation')
    display = False
    btntofilter = True
    context = {'voc' : voc, 'filter': filter, 'display' : display, 'btntofilter' : btntofilter}
    return render(request, 'english_to_swahili.html', context)

def etssort(request):
    voc = Vocabulary.objects.order_by('english_translation')
    filter = WordFilter(request.GET, queryset=Vocabulary.objects.all())
    voc = filter.qs.order_by('english_translation')
    display = True
    btntofilter = False
    filterpage = 'ets'
    context = {'voc' : voc, 'filter': filter, 'display' : display, 'btntofilter' : btntofilter, 'filterpage' : filterpage}
    return render(request, 'english_to_swahili.html', context)

def edit(request):
    voc = Vocabulary.objects.order_by('swahili_word')
    filter = WordFilter(request.GET, queryset=Vocabulary.objects.all())
    voc = filter.qs.order_by('swahili_word')
    display = False
    btntofilter = True
    context = {'voc' : voc, 'filter': filter, 'display' : display, 'btntofilter' : btntofilter}
    return render(request, 'edit.html', context)

def editsort(request):
    voc = Vocabulary.objects.order_by('swahili_word')
    filter = WordFilter(request.GET, queryset=Vocabulary.objects.all())
    voc = filter.qs.order_by('swahili_word')
    display = True
    btntofilter = False
    filterpage = 'edit'
    context = {'voc' : voc, 'filter': filter, 'display' : display, 'btntofilter' : btntofilter, 'filterpage' : filterpage}
    return render(request, 'edit.html', context)

def create_word(request):
    form = VocabularyForm()
    if request.method == 'POST':
        form = VocabularyForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('home.html')
    context = { 'form' : form}
    return render(request, 'add.html', context)

def update_word(request, pk):
    word = Vocabulary.objects.get(id=pk)
    form = VocabularyForm(instance=word)
    if request.method == 'POST':
        form = VocabularyForm(request.POST, instance=word)
        if form.is_valid():
            form.save()
            return redirect('edit')
        return redirect('edit')
    context = { 'form': form }
    return render(request, 'edit_form.html', context)

def delete_word(request, pk):
    word = Vocabulary.objects.get(id=pk)
    form = VocabularyForm(instance=word)
    if request.method == 'POST':
        word.delete()
        return redirect('edit')
    context = { 'form': form, 'word' : word }
    return render(request, 'delete_form.html', context)