from django.contrib import admin
from django.urls import path
from .views import homeview

app_name = 'home'

urlpatterns = [
    path('', homeview, name='home'),
]