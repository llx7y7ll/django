#premite un mismo formulario en varias plantillas

from .forms import LoginForm

def login_form_context(request):
    """
    Agrega el formulario de login al contexto de todas las plantillas.
    """
    form = LoginForm()
    return {'login_form': form}


def theme_processor(request):
    """
    Inyecta la variable 'current_theme' del contexto de la sesión en todos los templates.
    """
    return {'current_theme': request.session.get('theme', 'light')}