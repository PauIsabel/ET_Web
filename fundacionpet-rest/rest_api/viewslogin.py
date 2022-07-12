from contextlib import redirect_stderr
import token
from tokenize import Token
from urllib import request
from django.shortcuts import redirect, render
#Importar la vista generica 
from rest_framework import generics
#Importar el MODELO PERSONA
from core.models import Persona
#Importar el SERIALIZERS PERSONA
from .serializers import PersonaSerializer
from django.contrib import messages
from core.views import index

#Importar para el LOGIN
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator 
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
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


'''
VISTAS
'''
#Crear la vista para el MODELO PERSONA
#Vista basada en clases

    

#Crear el LOGIN
#Vista basada en clases
class Login(FormView):
    template_name = "registration/login.html"
    form_class = AuthenticationForm
    #success_url = reverse_lazy('core:index')
    success_url = reverse_lazy('rest_api:index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            #messages.success(request, "Ha iniciado sesión correctamente")
            #return HttpResponseRedirect(redirect_to='/')
            return HttpResponseRedirect(self.get_success_url())
            
        else:
            
            return super(Login,self).dispatch(request,*args,**kwargs) 

    #Validacion Login con TOKEN
    def form_valid(self, form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        #Aqui se valida el TOKEN asociado al usuario y si no tiene uno lo crea
        token,_ = Token.objects.get_or_create(user = user)

        if token:
            login(self.request, form.get_user())
            
            return super(Login, self).form_valid(form)
            

#Crear el LOGOUT
#Cada vez que se desloguee, eliminar el TOKEN
class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        
        logout(request)
        #despues de logout destruye el token y redirecciona a home
        messages.success(request, "Ha cerrado sesión correctamente")
        return HttpResponseRedirect(redirect_to='/')
        #Para probar en api/logout
        #return Response(status = status.HTTP_200_OK)

"""
class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        
        logout(request)
        
        return Response(status = status.HTTP_200_OK)
"""















'''
@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)
    username = data['username']
    password = data['password']
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(("Usuario invalido"), status=status.HTTP_400_BAD_REQUEST)
    pass_valido = check_password(password, user.password)
    if not pass_valido:
        return Response(("Password incorrecto"), status=status.HTTP_400_BAD_REQUEST)
        
    if user.is_active: 
        token, created = Token.objects.get_or_create(user=user)
        if created:
            return Response ({
                'token': token.key,
                'user': data,
                'message' : 'Inicio de sesión Exitoso'
            }, status=status.HTTP_200_OK)
        else:
            token.delete()
            token = Token.objects.create(user=user)
            return Response ({
                'token': token.key,
                'user': data,
                'message' : 'Inicio de sesión Exitoso'
            }, status=status.HTTP_200_OK)

    print(token.key)
    return Response(token.key)
'''



