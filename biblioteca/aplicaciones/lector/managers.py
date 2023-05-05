from django.db import models
from django.db.models import Q, Count, Avg, Sum
from django.db.models.functions import Lower

class PrestamoManager(models.Manager):
    # Prmedio de edad de los lectores
    def libros_promedio_edades(selt):
        resultado = selt.filter(
            libro__id = '1'
        ).aggregate(
            promedio_edad = Avg('lector__edad'),
            suma_edad = Sum('lector__edad')
        )
        return resultado
    
    def libros_promedio_edades(selt):
        resultado = selt.values(
            # valores por el cual se desea tomar 
            'libro'
        ).annotate(
            num_prestados = Count('libro'),
            #Accediendo al forenkey del modelo
            #Lower convierte el titulo del libre
            titulo = Lower('libro__titulo'),
        )
        for r in resultado:
            print("="*48)
            print(r, r['num_prestados'])
        return resultado
   