from django.shortcuts import render, redirect
from .models import Pizza, Comentario
from .forms import ComentarioForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
from django.http import HttpResponse

#este metodo devuelve todas las pizzas
#almacenadas en SQLite
def query_pizzas():
    pizzas = Pizza.objects.all()
    return pizzas

def index(request):
    pizzas = query_pizzas()
    context = {'pizzas': pizzas}
    return render(request, 'pizzeria/index.html')

def nuestras_pizzas(request):
    #selecciona todas las pizzas en la bbdd sqlite
    pizzas = query_pizzas()
    context = {'pizzas': pizzas}
    #se las pasamos al html
    return render(request, 'pizzeria/nuestras_pizzas.html', context)

def mostrar_info_pizza(request, id_pizza):
    #pizza seleccionada (requested)
    req_pizza = Pizza.objects.get(id = id_pizza)
    pizzas = Pizza.objects.all()
    context = {'req_pizza': req_pizza,'pizzas':pizzas}
    return render(request, 'pizzeria/nuestras_pizzas.html', context)

def contacto (request):
    return render(request, 'pizzeria/contacto.html')

@login_required
def dejar_comentario(request):
    if request.method != 'POST':
        #seleccionamos los comentarios
        comentarios = Comentario.objects.all()
        form = ComentarioForm()
    else:
        form = ComentarioForm(data = request.POST)
        if form.is_valid():
            #le añadimos el usuario al comentario nuevo
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.usuario = request.user
            nuevo_comentario.save()
            return redirect('pizzeria:index')
    context = {'form': form, 'comentarios': comentarios}
    return render(request, 'pizzeria/dejar_comentario.html', context)


#REVISAR MAS TARDE
@login_required
def editar_comentario(request, id_comentario):
    comentario = Comentario.objects.get(id = id_comentario)
    if comentario.usuario !=request.user:
        raise Http404
    if request.method != 'POST':
        #recogemos todos los comentario para mostrarlos
        comentarios = Comentario.objects.all()
        form =ComentarioForm()
        form.comentario = comentario.comentario
    else:
        if form.is_valid():
            comentario.comentario = form.comentario
            comentario.update()
    context = {'form': form, 'comentarios': comentarios}
    return render(request, 'pizzeria/dejar_comentario.html', context)

    
@login_required
def borrar_comentario(request, id_comentario):
    comentario = Comentario.objects.get(id = id_comentario)
    if comentario.usuario != request.user:
        raise Http404

    #metodo post
    #html no acepta ni DELETE ni PUT
    if request.method =='POST':
        comentario.delete()
        return redirect('pizzeria:dejar_comentario')


def carrito(request):
    return render(request, 'pizzeria/carrito.html')
    
   
        


