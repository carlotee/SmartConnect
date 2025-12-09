from rest_framework import viewsets
from .models import Sensor, Barrera, Departamento 
from .serializers import SensorSerializer, BarreraSerializer 
from usuarios.permissions import IsAdminOrReadOnly, CustomIsAuthenticated 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

class SensorViewSet(viewsets.ModelViewSet):
    """
    API CRUD para la gestión de Sensores. Aplica validaciones de MAC única y estado.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
    permission_classes = [AllowAny]
    
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({"detail": "Sensor no encontrado."}, status=status.HTTP_404_NOT_FOUND)


class BarreraViewSet(viewsets.ModelViewSet):
    queryset = Barrera.objects.all()
    serializer_class = BarreraSerializer
    
    permission_classes = [CustomIsAuthenticated, IsAdminOrReadOnly]
    
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({"detail": "Barrera no encontrada."}, status=status.HTTP_404_NOT_FOUND)