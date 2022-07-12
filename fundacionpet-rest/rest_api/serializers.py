from asyncore import read
from core.models import Producto, Marca, Adopcion, Persona


#Aqui se serializan los MODELOS
#Convierte la info a un tipo de archivo de intercambio comun como JSON

#Importar SERIALIZERS
from dataclasses import field
from pyexpat import model
from rest_framework import serializers
#Importar el MODELO PERSONA
from core.models import Producto, Marca, Adopcion, Persona
from django.contrib.auth.models import User

#Crear un SERIALIZERS para PERSONA
class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = (
            'id',
            'nombre',
            'apellido'
        )

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    marca_id = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all(), source='marca')
    nombre_marca = serializers.CharField(read_only=True, source='marca.nombre')
    marca = MarcaSerializer(read_only=True)
    nombre = serializers.CharField(required=True, min_length=3)
    
    def validate_nombre(self,value):
        existe = Producto.objects.filter(nombre__iexact = value).exists()

        if existe:
            raise serializers.ValidationError("El nombre del producto ya existe, porfavor escoja otro.")
        return value
    
    class Meta:
        model = Producto
        fields = '__all__'


class AdopcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adopcion
        fields = '__all__'