from django.urls import path, include
from . import views

from rest_framework import routers
from . import views, models

router = routers.DefaultRouter()
router.register(r'pizzas', views.PizzaViewSet)
router.register(r'usuarios', views.UserViewSet)
router.register(r'comentarios', views.ComentarioViewSet)
router.register(r'direcciones', views.DireccionViewSet)

app_name = 'api'

urlpatterns = [
  path('',include(router.urls)),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
