from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main, name='index'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
]