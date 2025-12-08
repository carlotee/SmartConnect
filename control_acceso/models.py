from django.db import models
from gestion_dispositivos.models import Sensor, Barrera 

class Evento(models.Model):

    TIPOS_EVENTO = [
        ('acceso_sensor', 'Intento de Acceso con Sensor'), 
        ('manual_apertura', 'Apertura Manual'),            
        ('manual_cierre', 'Cierre Manual'),                
    ]

    RESULTADOS = [
        ('permitido', 'Acceso Permitido'),
        ('denegado', 'Acceso Denegado'),
        ('error', 'Error de Lectura'),
    ] 

    tipo = models.CharField(max_length=20, choices=TIPOS_EVENTO)
    
    sensor = models.ForeignKey(Sensor, on_delete=models.SET_NULL, null=True, blank=True)
    
    barrera = models.ForeignKey(Barrera, on_delete=models.SET_NULL, null=True, blank=True)

    resultado = models.CharField(max_length=20, choices=RESULTADOS, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True) 
    
    fecha_hora = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.tipo} - {self.fecha_hora}"
    