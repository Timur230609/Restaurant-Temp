from django.db import models
#from ckeditor.fields import RichTextField
#from hitcount.models import HitCountMixin,HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator    


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    content = models.TextField()