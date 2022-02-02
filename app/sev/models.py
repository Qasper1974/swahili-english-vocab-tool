from django.db import models

# Create your models here.
class Vocabulary(models.Model):
    swahili_word = models.CharField(max_length=55, blank=False, default='')
    english_translation = models.CharField(max_length=55, blank=False, default='')
    lesson = models.IntegerField()
    known = models.BooleanField(default=False)

