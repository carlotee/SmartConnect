from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioPersonalizado(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('operador', 'Operador'),
    )
    
    rol = models.CharField(max_length=20, choices=ROLES, default='operador')
    
    rut = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.get_rol_display()}"