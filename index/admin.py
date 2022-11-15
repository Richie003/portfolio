from django.contrib import admin
from .models import Category, Contact, BlogContent

# Register your models here.
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(BlogContent)