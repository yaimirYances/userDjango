from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    
    def BuscarAutorNombre(self, nombre):
        resultado = self.filter(
            nombre__icontains = nombre
        )
        return resultado
    
    def BuscarAutorNombre_Apellidos(self, nombre):
        resultado = self.filter(
            Q(nombre__icontains = nombre) | Q(apellidos__icontains = nombre)
        )
        return resultado
    
    def BuscarAutorNombre_Edad(self, nombre):
        resultado = self.filter(
            nombre__icontains = nombre
        ).exclude(edad=25)
        return resultado
    
    def BuscarAutorNombre_Mayor(self, nombre):
        resultado = self.filter(
            edad__gt = 40, # Mayor que
            edad__lt = 56 # Menor que
        ).order_by("nombre")
        return resultado