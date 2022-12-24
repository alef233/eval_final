from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return Response ({'error': 'Por favor ingrese usuario y/o contraseÑa en conjunto'}, status=status.HTTP_400_BAD_REQUEST)
    #intentar hacer login con los datos de la BD
    user = authenticate(username=username, password=password)

    if not user:
        return Response ({'error': 'Credenciales no validas'}, status=status.HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)
    return Response ({'token': token.key}, status=status.HTTP_200_OK)

