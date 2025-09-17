from django.contrib import admin
from .models import Autor, Tematica, Articulo, ArticuloAutor
from django.contrib.auth.models import User

# Define the inline class for the Article-Author relationship
class ArticuloAutorInline(admin.TabularInline):
    model = ArticuloAutor
    extra = 1
    autocomplete_fields = ['autor']

# Define the admin class for the Article model
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tematica', 'dia_de_publicacion')
    list_filter = ('tematica', 'dia_de_publicacion')
    search_fields = ('titulo', 'tematica__titulo')
    inlines = [ArticuloAutorInline]

# Define the admin class for the Author model and add search fields
class AutorAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'apellidos', 'email') # <-- Add this line

# Register the models with the admin site
admin.site.register(Autor, AutorAdmin)
admin.site.register(Tematica)
admin.site.register(Articulo, ArticuloAdmin)