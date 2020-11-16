from django.shortcuts import render
from rest_framework import viewsets, permissions
from pizzeria import models
from api import models
from pizzeria.models import Pizza, Comentario, Direccion
from django.contrib.auth.models import User
from .models import PizzaSerializer, DireccionSerializer, ComentarioSerializer, UserSerializer

# Create your views here.


class PizzaViewSet(viewsets.ModelViewSet):

    #API, permite ver y editar las pizzas 

    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = [permissions.IsAuthenticated]

class DireccionViewSet(viewsets.ModelViewSet):

    #API, permite ver y editar las direcciones

    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    permission_classes = [permissions.IsAuthenticated]

class ComentarioViewSet(viewsets.ModelViewSet):

    #API, permite ver y editar los comentarios

    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):

    #API, permite ver y editar los usuarios

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

