from django.urls import path
from mundial_api import views


urlpatterns = [
    path('equipo/<int:id>', views.mostrarEquipo),
    path('jugador/editar/<int:id>', views.gestionarJugador)
]