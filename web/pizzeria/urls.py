from django.urls import path

from . import views

app_name = 'pizzeria'

urlpatterns = [
    path('', views.index, name='index'),
    path('nuestras_pizzas', views.nuestras_pizzas, name='nuestras_pizzas'),
    path('contacto', views.contacto, name='contacto'),
    path('dejar_comentario', views.dejar_comentario, name='dejar_comentario'),
    path('carrito', views.carrito, name = 'carrito'),
    #en esta ruta le pasamos el parametro del id de comentario
    path('editar_comentario/<int:id_comentario>', views.editar_comentario, name='editar_comentario'),
    path('borrar_comentario/<int:id_comentario>', views.borrar_comentario, name='borrar_comentario'),
    path('mostrar_info_pizza/<int:id_pizza>', views.mostrar_info_pizza, name = 'mostrar_info_pizza'),
]