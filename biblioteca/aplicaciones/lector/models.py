from django.db import models
from aplicaciones.libro.models import Libro
# Create your models here.

class Lector(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    edad = models.PositiveBigIntegerField()

    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectors'

    def __str__(self):
        return self.nombre


class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()
    
    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'

    def __str__(self):
        return self.libro.titulo
