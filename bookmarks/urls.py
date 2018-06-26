from django.urls import path
from . import views

urlpatterns = [
  #ex: /bookmarks
  path('', views.index, name='index')
]