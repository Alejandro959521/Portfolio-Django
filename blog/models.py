from django.db import models
import datetime 
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images')
    date = models.DateField(datetime.date.today)

