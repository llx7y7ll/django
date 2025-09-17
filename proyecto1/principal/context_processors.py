#premite un mismo formulario en varias plantillas

from .forms import LoginForm

def login_form_context(request):
    """
    Agrega el formulario de login al contexto de todas las plantillas.
    """
    form = LoginForm()
    return {'login_form': form}