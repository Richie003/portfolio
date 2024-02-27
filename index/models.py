from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.utils.timezone import now

# Create your models here.
# Services Category.
class Category(models.Model):
    categories = models.CharField(default='', max_length=100, blank=False, null=True)

    def __str__(self):
        return str(self.categories)

#Contact.
class Contact(models.Model):
    email = models.EmailField(default='', max_length=225, blank=False, null=True)
    message = models.TextField(default='', max_length=300, blank=False, null=False, auto_created=True)
    date_sent = models.DateTimeField(default=now)
    schedule = models.DateTimeField()

    def __str__(self):
        return str(f'message from {self.email}')
    
    class Meta:
        ordering = ['-schedule', '-date_sent']

class WhatsNew(models.Model):
    name = models.CharField(default='', max_length=100, blank=False, null=True)
    thumbnail_image = models.ImageField(upload_to="thumbnails/")
    body = RichTextField()
    new = models.BooleanField(default=True)
    added = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-added', '-updated']