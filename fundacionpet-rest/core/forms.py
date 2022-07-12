from dataclasses import fields
from pickle import TRUE
from pyexpat import model
from tabnanny import verbose
from django import forms
from .models import Contacto1, Producto, Adopcion,ContactoAdopcion,Suscripcion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings

#Formulario Contacto1
class Contacto1Form(forms.ModelForm):
    #Validando los campos
    nombre = forms.CharField(min_length=3, max_length=50)

    class Meta:
        model = Contacto1
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'

#Formulario para agregar producto
class ProductoForm(forms.ModelForm):

    #Validando los campos
    nombre = forms.CharField(min_length=3, max_length=50)
    precio = forms.IntegerField(min_value=1000, max_value=1200000)
    precio_oferta = forms.IntegerField(min_value=0, max_value=1500000)
    stock = forms.IntegerField(min_value=1, max_value=300)
    nuevo = forms.BooleanField(required=False)

    class Meta:
        model = Producto
        fields = '__all__'
    
        #Para las fechas de agregar producto
        # widgets = {
        #     "fecha_fabricacion": forms.SelectDateWidget()
        # }

#Formulario Registro Usuario -> Para validar sus campos
class RegistroUserCreationForm(UserCreationForm):

    #Validando los campos
    first_name = forms.CharField(min_length=3, max_length=50,label="Nombre") 
    last_name = forms.CharField(min_length=3, max_length=50,label="Apellido")
    email = forms.CharField(min_length=3, max_length=50,label="Correo")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password1', 'password2']


class AdopcionForm(forms.ModelForm):
    opciones_tamaño = [
        ['', '--'],
        ['0', 'Pequeño'],
        ['1', 'Mediano'],
        ['2', 'Grande'],
    ]
    opciones_sexo = [
    ['', '--'],
    [0, "Macho"],
    [1, "Hembra"],
    ]

    nombre = forms.CharField(min_length=2, max_length=50,label="Nombre",help_text="Ingrese el nombre de la mascota en adopción")
    tamanio = forms.ChoiceField(label="Tamaño",choices=opciones_tamaño)
    edad = forms.IntegerField(min_value=1, max_value=50,label="Edad",help_text="Ingrese edad entre 1 y 50 años")
    sexo = forms.ChoiceField(label="Sexo",choices=opciones_sexo)
    microchip = forms.CharField(min_length=5, max_length=50,label="N° Microchip",help_text="Ingrese N° de MicroChip")
    vacunado = forms.BooleanField(required=False,label="¿Vacunas al día?")
    
    class Meta:
        model = Adopcion
        fields = '__all__'



#Formulario ContactoADOPCION
class ContactoAdopcionForm(forms.ModelForm):
    #Validando los campos
    nombre = forms.CharField(min_length=3, max_length=50)
    suscripcion = forms.BooleanField(required=False,label="¿Desea suscribirse con ayuda?")

    class Meta:
        model = ContactoAdopcion
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
        

class SuscripcionForm(forms.ModelForm):
    email = forms.EmailField(label="Porfavor ingrese un correo de usuario registrado")
    suscripcion = forms.BooleanField(required=False,label="¿Desea suscribirse a una donación?")

    class Meta:
        model = Suscripcion
        fields =  ['email','suscripcion' ]
        
