from django.contrib import admin
from .models import Departamento, Barrera, Sensor

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Barrera)
class BarreraAdmin(admin.ModelAdmin):
    list_display = ('id', 'departamento', 'estado')
    list_filter = ('estado',)

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('mac_address', 'tipo', 'departamento', 'estado', 'fecha_creacion')
    list_filter = ('tipo', 'estado')
    search_fields = ('mac_address',)