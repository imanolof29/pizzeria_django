from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def perfil(request):
    return render(request, 'registration/perfil.html')

def registrarse(request):
    if request.method != 'POST':
        #form pre-creado por django
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            nuevo_usuario = form.save()
            login(request, nuevo_usuario)
            return redirect('pizzeria:index')
    context = {'form': form}
    return render(request, 'registration/registrarse.html', context)