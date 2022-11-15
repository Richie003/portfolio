from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Contact, Category, BlogContent

# Create your views here.
def home(request):
    context = {}
    return render(request, 'index/home.html', context)

def contact(request):
    category = Category.objects.all()
    context={
        'category':category
    }
    return render(request, 'index/contact.html', context)

def service(request):
    return render(request, 'index/services.html', {})

def getcontact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('fullname')
        project = request.POST.get('project')
        category = request.POST.getlist('category')
        new_list = [int(j) for e in category for j in e.split(',')]
        add_contact = Contact.objects.create(name=name, email=email, project=project, schedule=timezone.now() + timedelta(hours=1))
        add_contact.save()
        for obj in new_list:
            add_contact.category.add(obj)
        success = 'We would get back to you in an hour.'
        return HttpResponse(success)

# ------------- Blog Views Start -------------- #

def blog(request):
    context = {}
    return render(request, 'index/blog/blog.html', context)

def bloglist(request):
    blog_queryset = BlogContent.objects.all()
    data = []
    for i in blog_queryset:
        item = {
            'title': i.title,
            'body': i.body,
            'image': i.thumbnail_image.url,
            'updated': f'{i.updated.minute}min(s) ago'
        }
        data.append(item)
        print(data)
    return JsonResponse({'contents':data})
