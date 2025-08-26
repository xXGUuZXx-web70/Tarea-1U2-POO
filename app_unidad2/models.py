from django.db import models
class Autor(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Nacionalidad = models.CharField(max_length=50)
    Fecha_Nacimiento = models.DateField()
def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Libro(models.Model):
    Titulo = models.CharField(max_length=200)
    Fecha_Publicacion = models.DateField()
    Numero_Paginas = models.PositiveIntegerField()
    Autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="libros")

    def __str__(self):
        return self.titulo


class Editorial(models.Model):
    Nombre = models.CharField(max_length=150)
    Direccion = models.CharField(max_length=200)
    Pais = models.CharField(max_length=50)
    Libros = models.ManyToManyField(Libro, related_name="editoriales")

    def __str__(self):
        return self.nombre
# Create your models here.
