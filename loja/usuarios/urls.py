from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.usuarios, name='usuarios'),
    path('cadastro/', views.usuarioCadastro, name='usuarioCadastro'),
    path('setUsuario/', views.setUsuario, name='setUsuario'),
]