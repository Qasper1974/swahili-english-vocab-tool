from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ste/', views.ste),
    path('create_word/', views.create_word),

    path('', views.home),
]
