from rest_framework import serializers
from control_acceso.models import Evento
from gestion_dispositivos.models import Sensor, Barrera 

class SensorSerializer(serializers.ModelSerializer):
    departamento_nombre = serializers.ReadOnlyField(source='departamento.nombre', default=None)
    
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
        
        elif tipo in ['manual_apertura', 'manual_cierre']:
            data['resultado'] = 'permitido'
        
        return data