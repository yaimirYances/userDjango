from django.db import models
from aplicaciones.libro.models import Libro
from aplicaciones.autor.models import Persona
from .managers import PrestamoManager
# Create your models here.

class Lector(Persona):

    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'


class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name = "prestamosLibros")
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()
    
    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'
        
    objects = PrestamoManager()
    
    def save(self, *args, **kwargs):
        print("-"*25)
        self.libro.stock = self.libro.stock - 1
        self.libro.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.libro.titulo
