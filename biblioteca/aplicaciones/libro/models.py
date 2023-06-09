from django.db import models
from aplicaciones.autor.models import Autor
from django.db.models.signals import post_save

from PIL import Image

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
    stock = models.PositiveBigIntegerField(default=0)
    
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']
        
    objects = LibroManager()

    def __str__(self):
        return self.titulo


def optimize_image(sender, instance, **kwargs):
    print("*"*25)
    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality=20, optimize=True)
    
    
post_save.connect(optimize_image, sender=Libro)