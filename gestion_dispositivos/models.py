from django.db import models

class Departamento(models.Model):

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Barrera(models.Model):

    ESTADOS = [
        ('abierta', 'Abierta'),
        ('cerrada', 'Cerrada'),
    ]

    departamento = models.OneToOneField(Departamento, on_delete=models.CASCADE, related_name='barrera')
    estado = models.CharField(max_length=10, choices=ESTADOS, default='cerrada') #
    
    def __str__(self):
        return f"Barrera de {self.departamento.nombre} - {self.estado}"

class Sensor(models.Model):

    ESTADOS_SENSOR = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('bloqueado', 'Bloqueado'),
        ('perdido', 'Perdido'),
    ] #

    #aca sera el codigo unicoooo siosi
    mac_address = models.CharField(max_length=50, unique=True, verbose_name="Código UID/MAC")
    
    tipo = models.CharField(max_length=50, blank=True, null=True) # Ej: Tarjeta, Llavero

    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True)
    
    estado = models.CharField(max_length=20, choices=ESTADOS_SENSOR, default='inactivo')
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mac_address} ({self.estado})"