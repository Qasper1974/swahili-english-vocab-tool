from django.db import models

# Create your models here.
class Vocabulary(models.Model):
    swahili_word = models.CharField(max_length=50, blank=False, default='')
    english_translation = models.CharField(max_length=50, blank=False, default='')
    lesson = models.IntegerField()
    image_path = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=200, blank=False, default='')
    known = models.BooleanField(default=False)
