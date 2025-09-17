from django.urls import path
from . import views

urlpatterns = [
    path('contacto/', views.formulario_view, name='ContactForm'),
    path('home/', views.home, name='home'),
    path('contacto/exito/', views.contacto_correcto, name='contacto_correcto'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
