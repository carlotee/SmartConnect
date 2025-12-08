from rest_framework import serializers
from .models import UsuarioPersonalizado
from gestion_dispositivos.models import Departamento 

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = UsuarioPersonalizado
        fields = ('id', 'username', 'email', 'rol', 'rut', 'password')
        read_only_fields = ('rol',)

    def create(self, validated_data):
        user = UsuarioPersonalizado.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            rol=validated_data.get('rol', 'operador')
        )
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            validated_data.pop('password')
        return super().update(instance, validated_data)
    
class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'
        
    def validate_nombre(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El nombre del departamento debe tener al menos 3 caracteres.") 
        return value