from django.urls import path, include
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    #pagina de registro
    path('registrarse/', views.registrarse, name='registrarse'),
    path('perfil/', views.perfil, name='perfil'),
]
