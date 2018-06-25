from django.shortcuts import render
from . import views

# Create your views here.
urlpatterns = [
  path('', notes.index, name='index')
]
