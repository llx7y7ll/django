from django.urls import path
from . import views

urlpatterns = [
    path('formulario/', views.formulario_view, name='ContactForm'),
]
