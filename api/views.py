from django.shortcuts import render
from rest_framework.permissions import AllowAny 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny]) 
def api_info(request):
  return Response({
    "autor": ["Tu Nombre Apellido"],
    "asignatura": "Programación Back End",
    "proyecto": "SmartConnect API",
    "descripcion": "API RESTful para el control de acceso IoT.",
    "version": "1.0"
  })