from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import EventoSerializer 
from .models import Evento 
from usuarios.permissions import IsAdminOrReadOnly
from rest_framework.permissions import AllowAny

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all().order_by('-fecha_hora')
    serializer_class = EventoSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'post', 'head', 'options']
    
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({"Evento no encontrado."}, status=status.HTTP_404_NOT_FOUND)