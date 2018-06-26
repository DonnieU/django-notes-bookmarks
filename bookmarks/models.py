from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class Bookmark(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  name = models.CharField(max_length=200)
  url = models.URLField(max_length=200)
  date_added = models.DateTimeField(auto_now_add=True)

  # 'url' or 'folder -- taken from how Chrome delineates in its JSON Bookmarks file
  bookmark_type = models.CharField(max_length=6, choices=[('u', 'url'), ('f', 'folder')], default='u')

class PersonalBookmark(Bookmark):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
