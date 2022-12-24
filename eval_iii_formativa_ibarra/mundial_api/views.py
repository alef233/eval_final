from django.shortcuts import render
from mundial_api.models import Jugador
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import  IsAuthenticated
# Create your views here.
from .serializers import  JugadorSerializer 

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
#Me rindo no me sale con many para mostrar a los jugadores , solo muestra si hay un jugador poe equipo
def mostrarEquipo(request, id ,):
    try:
        Team = Jugador.objects.get(equipo = id)
        serializado = JugadorSerializer(Team)
        return Response(serializado.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['PATCH', 'DELETE', 'POST'])
@permission_classes((IsAuthenticated,))
#actualizar
def gestionarJugador(request, id):
    if request.method == 'PATCH':
        try:
            jugador = Jugador.objects.get(id=id)
            serializador = JugadorSerializer(jugador, data=request.data, partial=True)
            if serializador.is_valid():
                serializador.save()
                return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #eliminar 
    if request.method == 'DELETE':
        try:
            jugador = Jugador.objects.get(id=id)
            jugador.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

    #crear
    if request.method == 'POST':
        try:
            serializado = JugadorSerializer(data=request.data)
            if serializado.is_valid():
                serializado.save()
                return Response(serializado.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializado.errors, status=status.HTTP_400_BAD_REQUEST)    
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)