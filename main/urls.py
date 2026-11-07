from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('location/', views.location, name='location'),
    path('projects/', views.projects, name='projects'),
    path('services/', views.services, name='services'),
]