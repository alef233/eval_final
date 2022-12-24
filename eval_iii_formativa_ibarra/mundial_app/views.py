from django.shortcuts import render
from mundial_api.models import Equipo
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from mundial_api.models import Equipo

# Create your views here.

#mostar equipos
@csrf_exempt
@api_view(['GET'])
@permission_classes((AllowAny,))
def listaEquipos(request):
    equipo = Equipo.objects.all()
    data = {'equipo' : equipo}
    return render(request,'mundial_app_web/mundial_app_all.html',data)

@csrf_exempt
@permission_classes((AllowAny,))
def mostrarEquipoPage(request, id):
    try:
        equipo = Equipo.objects.filter(id=id).first
        data = {'equipo': equipo}
        return render(request,"mundial_app_web/mundial_app.html",data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)



