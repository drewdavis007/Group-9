from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'root'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
]