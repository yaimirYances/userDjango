from django.db import models
from django.db.models import Q

class LibroManager(models.Manager):
    
    def BuscarLibros_Fecha(self, nombre):
        resultado = self.filter(
            titulo__icontains = nombre,
        )
        return resultado
    
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
        
class CategoriaManager(models.Manager):
    def categoria_Autor(self, autor):
        return self.filter(
            categoriaLibro__autores__id = autor
        ).distinct()
    