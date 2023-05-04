from django.db import models
from aplicaciones.autor.models import Autor

# Create your models here.
from .managers import LibroManager, CategoriaManager

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    objects = CategoriaManager()

    def __str__(self):
        return self.nombre + " " + str(self.id)


class Libro(models.Model):
    # related_named se usa para comunicar los forenkey en el managers
    # de una una tabla a otra sin relacion alguna
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name = "categoriaLibro")
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField("Fecha de lanzamiento")
    portada = models.ImageField(upload_to="portada")
    visitas = models.PositiveBigIntegerField()
    
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        
    objects = LibroManager()

    def __str__(self):
        return self.titulo
