from django.shortcuts import render

# Create your views here.
from .forms import ContactForm  

def formulario_view(request):
    form = ContactForm()
    return render(request, 'principal/mi_formulario.html', {'form': form})
