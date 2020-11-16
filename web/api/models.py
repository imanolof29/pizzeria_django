from django.db import models
from pizzeria.models import Pizza, Comentario, Direccion
from rest_framework import serializers
from django.contrib.auth.models import User

# Create your models here.

class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pizza
        fields = ['id', 'nombre', 'precio']

class DireccionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direccion
        #mostramos el campo usuario_id y no el campo usuario
        fields = ['id', 'direccion', 'poblacion', 'usuario_id']


class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id','comentario', 'fecha_publicacion', 'usuario_id']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']



