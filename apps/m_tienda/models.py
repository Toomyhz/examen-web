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
    precio = models.FloatField()
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    genero = models.ManyToManyField(Genero, blank=True)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    consola = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre