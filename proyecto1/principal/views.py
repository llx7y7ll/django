from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .forms import ContactForm, LoginForm  

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
            return redirect('/principal/home') 
        else:
            # Si las credenciales no son válidas
            # Puedes añadir un mensaje de error al formulario
            form.add_error(None, "Nombre de usuario o contraseña incorrectos.")

    context = {'form': form}
    return render(request, 'principal/home', context)

def logout_view(request):
    logout(request)
    print("Usuario desconectado")
    return redirect('/principal/home') 