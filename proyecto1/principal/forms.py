from django import forms

class ContactForm(forms.Form):
	Nombre =  forms.CharField(max_length=100)
	Correo = forms.EmailField()
	Mensaje = forms.CharField(widget=forms.Textarea)
