from django.db import models

# Create your models here.
from .managers import AutorManager #Importando managers

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    edad = models.PositiveBigIntegerField()
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    objects = AutorManager()
    
    def __str__(self):
        return self.nombre + " " + self.apellidos + " " + str(self.id)