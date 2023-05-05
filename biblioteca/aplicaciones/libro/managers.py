from django.db import models
from django.db.models import Q
from django.db.models import Count

from django.contrib.postgres.search import TrigramSimilarity

class LibroManager(models.Manager):
    
    def BuscarLibros_Fecha(self, nombre):
        resultado = self.filter(
            titulo__icontains = nombre,
        )
        return resultado
    
    def BuscarLibros_Fecha_Triangulacion(self, nombre):
        if nombre:
            resultado = self.filter(
                titulo__trigram_similar = nombre,
            )
            return resultado
        else:
            return self.all() [:10]
    
    def BuscarLibros_FechaIF(self, nombre, fecha_i, fecha_f):
        resultado = self.filter(
            titulo__icontains = nombre,
            fecha__range = (fecha_i, fecha_f)
        )
        return resultado
    
    def BuscarLibros_Categoria(self, id):
        return self.filter(
            categoria__id = id
        ).order_by("titulo")
        
    # Manager para agregar un nuevo autor a un libro existente
    def agregarLibro(self, idLibro, autor):
        libro = self.get(id = idLibro)
        libro.autores.add(autor)
        return libro
    
    def libros_num_prestamos(self):
        resultado = self.aggregate(
            num_prestamos = Count('prestamosLibros')
        )
        return resultado
    
    def libros_promedio_edades(selt):
        resultado = selt.annotate(
            num_prestados = Count('prestamosLibros')
        )
        for r in resultado:
            print("="*48)
            print(r, r.num_prestados)
        return resultado
        
class CategoriaManager(models.Manager):
    def categoria_Autor(self, autor):
        return self.filter(
            categoriaLibro__autores__id = autor
        ).distinct()
    