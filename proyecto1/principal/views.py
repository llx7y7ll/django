from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.forms import modelformset_factory, inlineformset_factory
from .models import Autor, Tematica, Articulo, ArticuloAutor
# Create your views here.
from .forms import ContactForm, LoginForm, ThemeForm, AutorForm, TematicaForm

#def formulario_view(request):
#    form = ContactForm()
#    return render(request, 'principal/mi_formulario.html', {'form': form})

def formulario_view(request):
    if request.method == 'POST':

        print("Datos recibidos en el POST:", request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            # Los datos son válidos, accede a ellos
            nombre = form.cleaned_data['Nombre']
            correo = form.cleaned_data['Correo']
            mensaje = form.cleaned_data['Mensaje']
            return redirect('contacto_correcto')
        else:
            print("Errores en el formulario:", form.errors)
    else:
        initial_data = {
            'Nombre': 'Tu Nombre',
            'Correo': 'ejemplo@correo.com',
            'Mensaje': 'Hola, este es un mensaje predeterminado.',
        }
        form = ContactForm(initial=initial_data)
    
    return render(request, 'principal/contacto.html', {'form': form})


def home(request):
    """
    Renderiza la página de inicio.
    """
    return render(request, 'principal/inicio.html', {})


def contacto_correcto(request):
    return render(request, 'principal/contacto_correcto.html')


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Si el usuario es válido, iniciar la sesión
            print("Usuario conectado:", user.username)
            login(request, user)
            # Redireccionar al home o a donde desees
            return redirect('login') 
        else:
            # Si las credenciales no son válidas
            # Puedes añadir un mensaje de error al formulario
            form.add_error(None, "Nombre de usuario o contraseña incorrectos.")

    context = {'form': form}
    return render(request, 'principal/login.html', context)

def logout_view(request):
    logout(request)
    print("Usuario desconectado")
    return render(request, 'principal/logout.html')




def config_view(request):

    print("Cambiando tema...")
    # Si la solicitud es un POST, procesamos el formulario
    if request.method == 'POST':
        form = ThemeForm(request.POST)
        if form.is_valid():
            # Obtenemos el tema seleccionado del formulario
            selected_theme = form.cleaned_data['theme']

            # Guardamos el tema en la variable de sesión
            request.session['theme'] = selected_theme
    else:
        # Si la solicitud es un GET, creamos una instancia del formulario
        current_theme = request.session.get('theme', 'light')
        form = ThemeForm(initial={'theme': current_theme})

    # Obtenemos el tema actual de la sesión (si no existe, usamos 'light' por defecto)
    current_theme = request.session.get('theme', 'light')
    
    context = {
        'form': form,
        'current_theme': current_theme,
    }

    return render(request, 'principal/config.html', context)




def publicaciones_view(request):
    # Creamos un FormSet para el modelo Autor
    AutorFormSet = modelformset_factory(Autor, form=AutorForm, extra=1)
    
    # Creamos un FormSet para el modelo Tematica
    TematicaFormSet = modelformset_factory(Tematica, form=TematicaForm, extra=1)

    if request.method == 'POST':
        # Instanciamos los FormSets con los datos del POST
        autor_formset = AutorFormSet(request.POST, request.FILES, prefix='autores')
        tematica_formset = TematicaFormSet(request.POST, request.FILES, prefix='tematicas')
        
        # Validamos ambos FormSets
        if autor_formset.is_valid() and tematica_formset.is_valid():
            autor_formset.save()
            tematica_formset.save()
            
            # Mensaje de éxito o redirección
            return redirect('publicaciones_view') # Redirige a la misma página para ver los cambios
    else:
        # Creamos los FormSets vacíos para el GET request
        autor_formset = AutorFormSet(prefix='autores')
        tematica_formset = TematicaFormSet(prefix='tematicas')

    context = {
        'autor_formset': autor_formset,
        'tematica_formset': tematica_formset,
    }
    
    return render(request, 'principal/publicaciones.html', context)