from django.urls import path
from index import views

urlpatterns = [
    path('', views.home, name='home'), 
    # URL for contact submission
    path('contact/', views.contact, name='contact'),
    path('contact_data/', views.create_contact, name='create_contact'),
    # URL for services
    path('services/', views.service, name='services'),
    # URL For Blog
    path('blog/stack/', views.SassDetail, name='blog'),
]