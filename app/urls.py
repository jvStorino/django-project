from django.contrib import admin
from django.urls import path
from .views import home, cadastrar, editar, update, delete, buscar_pessoa

urlpatterns = [
    path('', home, name='home'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('buscar/', buscar_pessoa, name='buscar_pessoa'),

]