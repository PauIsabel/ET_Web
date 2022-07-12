from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from pyexpat import model
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone


#Crear un MODELO para PERSONAS
class Persona(models.Model):
    #Crear los ATRIBUTOS
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=100)
    apellido = models.CharField('Apellido', max_length=200)

    #Vista por defecto para cada instancia del MODELO PERSONA
    def __str__(self):
        #Se formatea la cadena, muestra primero el apellido
        return '{0},{1}'.format(self.apellido, self.nombre) 


# Create your models here.
#TABLAS PROYECTO
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    precio_oferta = models.IntegerField()
    stock = models.IntegerField(null=True)
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre





    
#FORMULARIO CONTACTO
opciones_consulta = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencias"],
    [3, "Felicitaciones"]
]

class Contacto1(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    #avisos = models.BooleanField()

    def __str__(self):
        return self.nombre


opciones_tamanio = [
    [0, "Pequeño"],
    [1, "Mediano"],
    [2, "Grande"],
]


opciones_sexo = [
    [0, "Macho"],
    [1, "Hembra"],
]

class Adopcion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    tamanio = models.IntegerField(choices=opciones_tamanio)
    edad = models.IntegerField()
    sexo = models.IntegerField(choices=opciones_sexo)
    microchip = models.CharField(max_length=50)
    vacunado = models.BooleanField()
    imagen = models.ImageField(upload_to="adopciones", null=True)

    def __str__(self):
        return self.nombre


opciones_adopcion = [
    [0, "Adoptar"],
    [1, "Apadrinar"],
]

class ContactoAdopcion(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_adopcion = models.IntegerField(choices=opciones_adopcion)
    mensaje = models.TextField()
    suscripcion = models.BooleanField()

    def __str__(self):
        return self.nombre


class Suscripcion(models.Model):
    email = models.EmailField(User,null=True)
    suscripcion = models.BooleanField()
    fecha_vigencia = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
User

