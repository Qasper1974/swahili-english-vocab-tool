import django_filters

from .models import Vocabulary


class WordFilter(django_filters.FilterSet):
    class Meta:
        model = Vocabulary
        fields = ['swahili_word', 'english_translation', 'lesson']