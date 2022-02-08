from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ste/', views.ste, name="ste"),
    path('ets/', views.ets, name="ets"),
    path('edit/', views.edit, name="edit"),
    path('create_word/', views.create_word, name="create_word"),
    path('update_word/<str:pk>', views.update_word, name="update_word"),
    path('', views.home, name="home"),
]
