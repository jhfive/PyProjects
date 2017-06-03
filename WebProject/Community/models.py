from django.db import models

# Create your models here.
class Dto(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField(default='')
    url = models.URLField(default='')
    email = models.EmailField(default='')
    cdate = models.DateTimeField(auto_now_add=True)