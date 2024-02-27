from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from datetime import datetime, timedelta
from .models import *

# Create your views here.
def home(request):
    get_latest_saas = WhatsNew.objects.get(new=True)
    get_all_saas = WhatsNew.objects.all()
    context = {
        "saas":get_all_saas,
        "new_saas":get_latest_saas
    }
    return render(request, 'index/home.html', context)

def contact(request):
    category = Category.objects.all()
    context={
        'category':category
    }
    return render(request, 'index/contact.html', context)

def service(request):
    return render(request, 'index/services.html', {})

def create_contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        add_contact = Contact.objects.create(email=email, message=message, schedule=timezone.now() + timedelta(hours=1))
        add_contact.save()
        success = 'We would get back to you in an hour.'
        return HttpResponse(success)

# ------------- Blog Views Start -------------- #

def SassDetail(request):
    context = {}
    return render(request, 'index/blog/blog.html', context)

