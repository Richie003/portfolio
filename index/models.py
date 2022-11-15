from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.
# Services Category.
class Category(models.Model):
    categories = models.CharField(default='', max_length=100, blank=False, null=True)

    def __str__(self):
        return str(self.categories)

#Contact.
class Contact(models.Model):
    name = models.CharField(default='', max_length=100, blank=False, null=True)
    email = models.EmailField(default='', max_length=225, blank=False, null=True)
    category = models.ManyToManyField(Category)
    project = models.TextField(default='', max_length=300, blank=False, null=False, auto_created=True)
    date_sent = models.DateTimeField(auto_created=True, auto_now_add=True)
    schedule = models.DateTimeField()

    def __str__(self):
        return str(f'message from {self.name}')

class BlogContent(models.Model):
    title = models.CharField(max_length=50, default='', blank=False, null=True)
    slug = models.SlugField(blank=True)
    thumbnail_image = models.ImageField(upload_to="thumbnails/")
    body = RichTextField()
    added = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(f'title:\n{self.title}')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogContent, self).save(*args, **kwargs)