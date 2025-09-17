from django.db import models

ROL_CHOICES = [
    ('AUTOR_PRINCIPAL', 'Autor principal'),
    ('EDITOR', 'Editor'),
    ('REVISOR', 'Revisor'),
    ('COLABORADOR', 'Colaborador'),
]


class Autor(models.Model):
    """
    Modelo que representa a un autor.
    """
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'

class Tematica(models.Model):
    """
    Modelo que representa las temáticas o categorías de los artículos.
    """
    titulo = models.CharField(max_length=30)
    codigo = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.titulo

class Articulo(models.Model):
    """
    Modelo que representa un artículo de la revista.
    """
    titulo = models.CharField(max_length=100)
    # Relación Many-to-Many explícita con 'Autor' a través del modelo intermedio 'ArticuloAutor'
    autores = models.ManyToManyField(Autor, related_name='articulos', through='ArticuloAutor')
    # Relación ForeignKey a 'Tematica'
    tematica = models.ForeignKey(Tematica, on_delete=models.CASCADE)
    dia_de_publicacion = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        # Ordena los artículos por fecha de publicación de forma descendente
        ordering = ['-dia_de_publicacion']

    def __str__(self):
        return self.titulo

class ArticuloAutor(models.Model):
    """
    Modelo intermedio que define la relación Many-to-Many entre Articulo y Autor,
    permitiendo añadir campos adicionales a la relación.
    """
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    rol = models.CharField(
        max_length=50, 
        choices=ROL_CHOICES, # <-- Añadido
        blank=True, 
        null=True, 
        help_text="Selecciona el rol del autor en este artículo."
    )
    
    class Meta:
        # Evita que se repita la misma relación autor-artículo
        unique_together = ('autor', 'articulo')

    def __str__(self):
        return f'{self.autor.nombre} en {self.articulo.titulo}'