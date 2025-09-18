from django import forms
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Autor, Tematica, Articulo, ArticuloAutor


class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario", max_length=100)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

class ContactForm(forms.Form):
    Nombre = forms.CharField(
        max_length=100,
        required=True,
        help_text="Introduce tu nombre completo."
    )
    Correo = forms.EmailField(
        required=True,
        help_text="Introduce tu dirección de correo electrónico."
    )
    Mensaje = forms.CharField(
        widget=forms.Textarea,
        required=True,
        min_length=10,
        help_text="Introduce tu mensaje (mínimo 10 caracteres)."
    )
    Terminos_y_Condiciones = forms.BooleanField(
        required=True,
        label="Acepto los términos y condiciones"
    )

    def clean_Nombre(self):
        nombre = self.cleaned_data.get('Nombre')
        if not nombre.strip():
            raise ValidationError("El nombre no puede estar vacío.")
        return nombre

    def clean_Mensaje(self):
        mensaje = self.cleaned_data.get('Mensaje')
        if "http://" in mensaje or "https://" in mensaje:
            raise ValidationError("No se permiten enlaces en el mensaje.")
        return mensaje
    

class ThemeForm(forms.Form):
    # Opciones de temas disponibles
    THEME_CHOICES = [
        ('light', 'Claro'),
        ('dark', 'Oscuro'),
        ('blue', 'Azul'),
        ('green', 'Verde'),
    ]

    # El campo del formulario es un RadioSelect para que el usuario elija un tema
    theme = forms.ChoiceField(
        label="Seleccionar tema",
        choices=THEME_CHOICES,
        widget=forms.RadioSelect
    )
    

	
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class TematicaForm(forms.ModelForm):
    class Meta:
        model = Tematica
        fields = '__all__'