from django.db import models

# Create your models here.
from .managers import AutorManager #Importando managers

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    edad = models.PositiveBigIntegerField()
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        abstract = True #para que no se cree un modelo persona

    objects = AutorManager()
    
    def __str__(self):
        return self.nombre + " " + self.apellidos + " " + str(self.id)


class Autor(Persona):
    seudonimo = models.CharField("seudonimo", max_length=50, blank=True)
    objects = AutorManager()
    