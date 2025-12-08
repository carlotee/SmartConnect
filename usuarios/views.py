from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny 
from rest_framework import status
from .serializers import UsuarioSerializer, DepartamentoSerializer
from .models import UsuarioPersonalizado
from gestion_dispositivos.models import Departamento 
from .permissions import IsAdminOrReadOnly, CustomIsAuthenticated 

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

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = UsuarioPersonalizado.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [CustomIsAuthenticated, IsAdminOrReadOnly]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({"error": "Error de validación de usuario", "details": e.detail}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        return super().create(request, *args, **kwargs) 

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({"detail": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND)

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
  
    permission_classes = [CustomIsAuthenticated, IsAdminOrReadOnly]
    
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({"detail": "Departamento no encontrado."}, status=status.HTTP_404_NOT_FOUND)