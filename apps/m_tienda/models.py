from django.db import models
# Create your models here.

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Plataforma(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Tipo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='productos', null=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    genero = models.ManyToManyField(Genero, blank=True)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre