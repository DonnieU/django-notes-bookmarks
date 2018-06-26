from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Bookmark, PersonalBookmark

def index(request):
  context = { 'bookmarks': Bookmark.objects.all(),
              'personal_bookmarks': PersonalBookmark.objects.filter(user=request.user),
              'user': request.user,
  }
  template = loader.get_template('bookmarks/index.html')
  # return render(request, 'bookmarks/index.html', context)
  return HttpResponse(template.render(context, request))
