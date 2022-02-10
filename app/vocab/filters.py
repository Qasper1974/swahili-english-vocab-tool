import django_filters

from django_filters import CharFilter

from .models import Vocabulary


class WordFilter(django_filters.FilterSet):
    SwahiliWord = CharFilter(field_name='swahili_word', lookup_expr='icontains')
    EnglishTranslation = CharFilter(field_name='english_translation', lookup_expr='icontains')
    class Meta:
        model = Vocabulary
        fields = ['lesson']