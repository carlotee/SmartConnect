from rest_framework import serializers
from gestion_dispositivos.models import Sensor, Barrera 
from .models import Evento 


class SensorSerializer(serializers.ModelSerializer):
    departamento_nombre = serializers.ReadOnlyField(source='departamento.nombre')
    
    class Meta:
        model = Sensor
        fields = '__all__'
        
    def validate_mac_address(self, value):
        if len(value) < 5: 
            raise serializers.ValidationError("La MAC/UID debe tener al menos 5 caracteres.")
        return value

class BarreraSerializer(serializers.ModelSerializer):
    departamento_nombre = serializers.ReadOnlyField(source='departamento.nombre')

    class Meta:
        model = Barrera
        fields = '__all__'

    def validate_estado(self, value):
        valid_states = [choice[0] for choice in Barrera.ESTADOS] 
        
        if value not in valid_states:
            raise serializers.ValidationError(f"Estado de barrera no válido. Debe ser uno de: {', '.join(valid_states)}")
        
        return value

class EventoSerializer(serializers.ModelSerializer):
    sensor_mac = serializers.ReadOnlyField(source='sensor.mac_address', default='N/A')
    barrera_nombre = serializers.ReadOnlyField(source='barrera.departamento.nombre', default='N/A')

    class Meta:
        model = Evento
        fields = '__all__'
        read_only_fields = ('fecha_hora', 'resultado') 

    def validate(self, data):
        tipo = data.get('tipo')
        
        if tipo == 'acceso_sensor':
            sensor = data.get('sensor')
            
            if not sensor:
                raise serializers.ValidationError({"sensor": "ID de sensor no válido o no proporcionado."})
            
            if sensor.estado != 'activo':
                data['resultado'] = 'denegado'
            else:
                data['resultado'] = 'permitido'
        
        return data