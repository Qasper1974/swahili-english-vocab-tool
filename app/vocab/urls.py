from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ste/', views.ste, name="ste"),
    path('create_word/', views.create_word, name="create_word"),

    path('', views.home, name="home"),
]
