from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'resultado', 'sensor', 'barrera', 'fecha_hora')
    list_filter = ('tipo', 'resultado', 'fecha_hora')
    search_fields = ('tipo', 'resultado')
    readonly_fields = ('sensor', 'barrera', 'tipo', 'resultado', 'fecha_hora', 'descripcion')