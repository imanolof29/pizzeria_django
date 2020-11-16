from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Pizza(models.Model):
    nombre = models.CharField(max_length = 30)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    direccion = models.CharField(max_length=60)
    poblacion = models.CharField(max_length=20)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.direccion

class Comentario(models.Model):
    comentario = models.CharField(max_length=1000)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Pedido(models.Model):
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)

class Cesta(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE, primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete = models.CASCADE)





#insertar    
#pizza = Pizza(nombre='Pizza barbacoa', precio=9.9)
