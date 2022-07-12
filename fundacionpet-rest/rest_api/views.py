
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.parsers import JSONParser
from rest_framework import viewsets


import token
from tokenize import Token
from urllib import request
from django.shortcuts import redirect, render
#Importar la vista generica 
from rest_framework import generics
#Importar el MODELO PERSONA
from django.contrib.auth.models import User
from core.models import Producto, Marca, Adopcion, Persona
#Importar el SERIALIZERS PERSONA
from .serializers import ProductoSerializer,MarcaSerializer,AdopcionSerializer,PersonaSerializer, UsuarioSerializer

#Importar para el LOGIN
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator 
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token

#Importar los PERMISOS para proteger la info con LOGIN y TOKEN
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
#Logout
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

### Accede a las vistas desde http://127.0.0.1:8000/api/rest_api/usuario/",
### Estas vistas no son visibles con Token de Autenticacion mediante el ADVANCE REST CLIENT DE CHROME
class UsuarioViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]
    authentication_class = (TokenAuthentication)


###VISTA DE LOS SERIALIZER DE PERSONA EN FORMA DE VIEWSET
class PersonaList(generics.ListCreateAPIView):
    #SE INDICAN 2 PARAMETROS
    #CONSULTA: Para decir que dato debe traer
    queryset = Persona.objects.all()
    #Indica a Django Rest Framework el modelo serializado a usar 
    serializer_class = PersonaSerializer

    #Aqui se autentica con el LOGIN y TOKEN de forma personalizada
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

### Accede a las vistas desde http://127.0.0.1:8000/api/rest_api/persona/",
###VISTA DE LOS SERIALIZER DE PERSONA EN FORMA DE VIEWSET
class PersonaViewset(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [IsAuthenticated]
    authentication_class = (TokenAuthentication)

### Accede a las vistas desde http://127.0.0.1:8000/api/rest_api/marca/",
###VISTA DE LOS SERIALIZER DE MARCAS EN FORMA DE VIEWSET
class MarcaViewset(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [IsAuthenticated]
    authentication_class = (TokenAuthentication)

### Accede a las vistas desde http://127.0.0.1:8000/api/rest_api/producto/",
###VISTA DE LOS SERIALIZER DE PRODUCTOS EN FORMA DE VIEWSET
class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]
    authentication_class = (TokenAuthentication)

    def get_queryset(self):
        productos = Producto.objects.all()
        nombre = self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombre__contains=nombre)
        return productos

### Accede a las vistas desde http://127.0.0.1:8000/api/rest_api/adopcion/",
###VISTA DE LOS SERIALIZER DE ADOPCIONES EN FORMA DE VIEWSET
class AdopcionViewset(viewsets.ModelViewSet):
    queryset = Adopcion.objects.all()
    serializer_class = AdopcionSerializer
    permission_classes = [IsAuthenticated]
    authentication_class = (TokenAuthentication)

    def get_queryset(self):
        adopciones = Adopcion.objects.all()
        nombre = self.request.GET.get('nombre')

        if nombre:
            adopciones = adopciones.filter(nombre__contains=nombre)
        return adopciones       



###VISTA DE LOS SERIALIZER DE USUARIOS REGISTRADOS EN http://127.0.0.1:8000/api/lista_usuarios
@csrf_exempt
@api_view(['GET', 'POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated, ))
def lista_usuarios(request):
    if request.method == 'GET':
        usuario = User.objects.all()
        serializer = UsuarioSerializer(usuario, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

###VISTA DE LOS SERIALIZER DE USUARIOS REGISTRADOS EN http://127.0.0.1:8000/api/detalle_usuarios/<id>
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated, ))
def detalle_usuarios(request, id):
    permission_classes = [IsAuthenticated]
    authentication_class = (TokenAuthentication)
    try:
        usuario = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(usuario, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



###VISTA DE LOS SERIALIZER DE PRODUCTOS EN http://127.0.0.1:8000/api/lista_productos
@csrf_exempt
@api_view(['GET', 'POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated, ))
def lista_productos(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

###VISTA DE LOS SERIALIZER DE PRODUCTOS REGISTRADOS EN http://127.0.0.1:8000/api/detalle_productos/<id>
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated, ))
def detalle_productos(request, id):
    permission_classes = [IsAuthenticated]
    authentication_class = (TokenAuthentication)
    try:
        producto = Producto.objects.get(id=id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(producto, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





###VISTA DE LOS SERIALIZER DE ADOPCIONES EN http://127.0.0.1:8000/api/lista_adopciones
@csrf_exempt
@api_view(['GET', 'POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def lista_adopciones(request):
    if request.method == 'GET':
        adopcion = Adopcion.objects.all()
        serializer = AdopcionSerializer(adopcion, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdopcionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

###VISTA DE LOS SERIALIZER DE ADOPCIONES REGISTRADOS EN http://127.0.0.1:8000/api/detalle_adopciones/<id>
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated, ))
def detalle_adopciones(request, id):
    try:
        adopcion = Adopcion.objects.get(id=id)
    except Adopcion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AdopcionSerializer(adopcion)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AdopcionSerializer(adopcion, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        adopcion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



###VISTA DE LOS SERIALIZER DE MARCAS REGISTRADOS EN http://127.0.0.1:8000/api/lista_marcas
@csrf_exempt
@api_view(['GET', 'POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated, ))
def lista_marcas(request):
    if request.method == 'GET':
        marca = Marca.objects.all()
        serializer = MarcaSerializer(marca, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MarcaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

###VISTA DE LOS SERIALIZER DE MARCAS REGISTRADOS EN http://127.0.0.1:8000/api/detalle_marcas/<id>
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated, ))
def detalle_marcas(request, id):
    permission_classes = [IsAuthenticated]
    authentication_class = (TokenAuthentication)
    try:
        marca = Marca.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MarcaSerializer(marca)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MarcaSerializer(marca, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        marca.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)