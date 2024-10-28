from django.contrib import admin
from django.urls import path, include
from .views import home, cadastrar, editar, update

urlpatterns = [
    path('', home, name='home'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update')
]