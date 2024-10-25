from django.contrib import admin
from django.urls import path, include
from .views import home, cadastrar

urlpatterns = [
    path('', home, name='home'),
    path('cadastrar/', cadastrar, name='cadastrar')
]