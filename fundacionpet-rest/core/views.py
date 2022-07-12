from tokenize import Token
from rest_framework.authtoken.models import Token
import token
from rest_framework.decorators import api_view,permission_classes,authentication_classes

from rest_framework.parsers import JSONParser
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response

from unittest import expectedFailure
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Marca, Producto, Adopcion,Suscripcion
from .forms import Contacto1Form, ProductoForm, RegistroUserCreationForm,ContactoAdopcionForm,AdopcionForm,SuscripcionForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from core.cart import Cart,Wishlist, Compare
from django.contrib.auth.decorators import login_required, permission_required

# from django.views.generic import TemplateView

# Create your views here.
def base_1(request):
    productos = Producto.objects.all()
    data = {
        'productosTienda': productos,
    }
    return render(request, 'core/base_1.html',data)

def index(request):
    return render(request, 'core/index.html')

def error_404(request):
    return render(request, 'core/error_404.html')

def blog(request):
    return render(request, 'core/blog.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def adopcion_mascota(request):
    mascota = Adopcion.objects.all()
    #Paginacion
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(mascota, 20)
        mascota = paginator.page(page)
    except:
        raise Http404
    #Variable
    data = {
        'mascotaAdopcion': mascota,
        #Paginacion
        'paginator': paginator
    }
    return render(request, 'core/adopcion_mascota.html', data)

def contacto_adopcion(request):
    data = {
        'form': ContactoAdopcionForm()
    }
    if(request.method == "POST"):
        formulario = ContactoAdopcionForm(data=request.POST)
        if(formulario.is_valid()):
            formulario.save()
            messages.success(request, "Mensaje enviado exitosamente")

            #Para limpiar la pag. una vez enviado el mensaje
            return redirect('adopcion_mascota')
        else:
            messages.error(request, "No se ha podido enviar su mensaje, intente nuevamente")
            data["form"] = formulario

    return render(request, 'core/contacto_adopcion.html', data)

#FORMULARIOS
def contacto1(request):
    data = {
        'form': Contacto1Form()
    }
    if(request.method == "POST"):
        formulario = Contacto1Form(data=request.POST)
        if(formulario.is_valid()):
            formulario.save()
            messages.success(request, "Mensaje enviado exitosamente")

            #Para limpiar la pag. una vez enviado el mensaje
            return redirect('index')
        else:
            messages.error(request, "No se ha podido enviar su mensaje, intente nuevamente")
            data["form"] = formulario

    return render(request, 'core/contacto1.html', data)

@login_required(login_url='/login/')
def mi_cuenta(request):
    return render(request, 'core/mi_cuenta.html')


@login_required(login_url='/login/')
def mi_cuenta_CRUD(request):
    return render(request, 'core/mi_cuenta_CRUD.html')


@login_required(login_url='/login/')
def carro(request):
    productos = Producto.objects.all()
    data = {
        'productosTienda': productos,
    }
    return render(request, 'core/carro.html',data)

@login_required(login_url='/login/')
def checkout(request):
    return render(request, 'core/checkout.html')

@login_required(login_url='/login/')
def wishlist(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 10)
        productos = paginator.page(page)
    except:
        raise Http404
    data = {
        'productosTienda': productos,
        'paginator': paginator
    }
    return render(request, 'core/wishlist.html',data)

@login_required(login_url='/login/')
def compare(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 3)
        productos = paginator.page(page)
    except:
        raise Http404
    data = {
        'productosTienda': productos,
        'paginator': paginator
    }
    return render(request, 'core/compare.html',data)

@login_required(login_url='/login/')
def tiendafor(request):
    productos = Producto.objects.all()
    #Paginacion
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 12)
        productos = paginator.page(page)
    except:
        raise Http404
    #Variable
    data = {
        'productosTienda': productos,
        #Paginacion
        'paginator': paginator
    }
    return render(request, 'core/tiendafor.html', data)

##REGISTRO USUARIO CREA TOKEN AL REGISTRARSE Y DEVUELVE AL HOME
def registro_usuario(request):
    #Para enviarlo al template
    data = {
        'form': RegistroUserCreationForm()
    }
    #Validar metodo POST
    if(request.method == 'POST'):
        formulario = RegistroUserCreationForm(data=request.POST)
        if(formulario.is_valid()):
            formulario.save()
            #Autenticar usuario
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            token,_ = Token.objects.get_or_create(user = user)
            #Para que el usuario quede logueado
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            #Redirigir al index
            return redirect('index')
        else:
            data["form"] = formulario
    return render(request, 'registration/registro_usuario.html', data)

@login_required(login_url='/login/')
def order(request):
    return render(request, 'core/order.html')


#CRUD DE PRODUCTOS ADMIN
@permission_required('fundacionpet.view_producto')
def listar_producto(request):
    productos = Producto.objects.all()
    #Paginacion
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404
    #Variable
    data = {
        'productosTienda': productos,
        #Paginacion
        'paginator': paginator
    }
    return render(request, 'core/crud/listar_producto.html', data)

@permission_required('fundacionpet.add_producto')
def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }
    if(request.method == "POST"):
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if(formulario.is_valid()):
            formulario.save() 
            messages.success(request, "Producto registrado correctamente")
            #Para limpiar la pag. una vez agregado el producto
            return redirect('/mi_cuenta_CRUD')
        else:
            messages.error(request, "No se ha podido agregar el producto, intente nuevamente")
            data["form"] = formulario
    return render(request, 'core/crud/agregar_producto.html', data)

@permission_required('fundacionpet.change_producto')
def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'form':ProductoForm(instance=producto)
    }
    if(request.method == 'POST'):
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if(formulario.is_valid()):
            formulario.save()
            messages.success(request, "Registro modificado correctamente" )
            return redirect('/listar_producto')
        else:
            messages.error(request, "El producto no se ha podido modificar" )
            data['form'] = formulario
    return render(request, 'core/crud/modificar_producto.html', data)

@permission_required('fundacionpet.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    try:
        producto.delete()
        messages.success(request, "Producto eliminado exitosamente")
    except:
        messages.error(request, "El producto no se ha podido eliminar")
    return redirect('/listar_producto')




#AGREGAR PRODUCTO AL CARRO
def agregar_products(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.agregar(producto)
    messages.success(request, "Producto agregado al carro")
    return redirect("tiendafor")

def agregar_productsCart(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.agregar2(producto)
    return redirect("carro")

def eliminar_products(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.eliminar(producto)
    return redirect("carro")

def restar_products(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.restar(producto)
    return redirect("carro")

def limpiar_carrito(request):
    cart = Cart(request)
    cart.limpiar()
    return redirect("carro")




#AGREGAR PRODUCTO AL WISHLIST
def agregar_productsW(request, producto_id):
    wish = Wishlist(request)
    producto = Producto.objects.get(id=producto_id)
    wish.agregarW(producto)
    messages.success(request, "Agregado a su Lista de Deseos")
    return redirect("tiendafor")

def agregar_productsWMVC(request, producto_id):
    wish = Wishlist(request)
    producto = Producto.objects.get(id=producto_id)
    wish.agregarW2(producto)
    return redirect("wishlist")

def eliminar_productsW(request, producto_id):
    wish = Wishlist(request)
    producto = Producto.objects.get(id=producto_id)
    wish.eliminarW(producto)
    return redirect("wishlist")

def restar_productsW(request, producto_id):
    wish = Wishlist(request)
    producto = Producto.objects.get(id=producto_id)
    wish.restarW(producto)
    return redirect("wishlist")

def limpiar_carritoW(request):
    wish = Wishlist(request)
    wish.limpiarW()
    return redirect("wishlist")



#AGREGAR PRODUCTO AL COMPARE
def agregar_productsC(request, producto_id):
    compare = Compare(request)
    producto = Producto.objects.get(id=producto_id)
    compare.agregarC(producto)
    messages.success(request, "Agregado al comparador")
    return redirect("tiendafor")

def agregar_productsCMVC(request, producto_id):
    compare = Compare(request)
    producto = Producto.objects.get(id=producto_id)
    compare.agregarC2(producto)
    return redirect("compare")

def eliminar_productsC(request, producto_id):
    compare = Compare(request)
    producto = Producto.objects.get(id=producto_id)
    compare.eliminarC(producto)
    return redirect("compare")

def restar_productsC(request, producto_id):
    compare = Compare(request)
    producto = Producto.objects.get(id=producto_id)
    compare.restarC(producto)
    return redirect("compare")

def limpiar_carritoC(request):
    compare = Compare(request)
    compare.limpiarC()
    return redirect("compare")



#AGREGANDO MASCOTAS PARA ADOPCIONES
#CRUD ADOPCIONES
@permission_required('fundacionpet.view_adopcion')
def listar_mascota(request):
    mascotas = Adopcion.objects.all()
    #Paginacion
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(mascotas, 5)
        mascotas = paginator.page(page)
    except:
        raise Http404
    #Variable
    data = {
        'mascotaAdopcion': mascotas,
        #Paginacion
        'paginator': paginator
    }
    return render(request, 'core/crud/listar_mascota.html', data)

@permission_required('fundacionpet.add_adopcion')
def agregar_mascota(request):
    data = {
        'form': AdopcionForm()
    }
    if(request.method == "POST"):
        formulario = AdopcionForm(data=request.POST, files=request.FILES)
        if(formulario.is_valid()):
            formulario.save() 
            messages.success(request, "Mascota registrada correctamente")
            return redirect('/mi_cuenta_CRUD')
        else:
            messages.error(request, "No se ha podido agregar mascota, intente nuevamente")
            data["form"] = formulario
    return render(request, 'core/crud/agregar_mascota.html', data)

@permission_required('fundacionpet.change_adopcion')
def modificar_mascota(request, id):
    mascota = get_object_or_404(Adopcion, id=id)
    data = {
        'form':AdopcionForm(instance=mascota)
    }
    if(request.method == 'POST'):
        formulario = AdopcionForm(data=request.POST, instance=mascota, files=request.FILES)
        if(formulario.is_valid()):
            formulario.save()
            messages.success(request, "Registro modificado correctamente" )
            return redirect('/listar_mascota')
        else:
            messages.error(request, "El registro no se ha podido modificar" )
            data['form'] = formulario
    return render(request, 'core/crud/modificar_mascota.html', data)

@permission_required('fundacionpet.delete_adopcion')
def eliminar_mascota(request, id):
    producto = get_object_or_404(Adopcion, id=id)
    try:
        producto.delete()
        messages.success(request, "Registro de Mascota eliminado exitosamente")
    except:
        messages.error(request, "El Registro no se ha podido eliminar")
    return redirect('/listar_mascota')


def agregar_suscripcion(request):
    data = {
        'form' : SuscripcionForm()
    }
    if(request.method == "POST"):
        formulario = SuscripcionForm(data=request.POST)
        if(formulario.is_valid()):
            formulario.save() 
            messages.success(request, "Suscrito correctamente")
            return redirect('index')
        else:
            messages.error(request, "No se ha podido suscribir, intente nuevamente")
            data["form"] = formulario
    return render(request, 'core/suscripcion.html', data)



from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

#CRUD DE SUSCRIPCION ADMIN
@login_required(login_url='/login/')
@permission_required('is_staff')
def listar_suscripciones(request):
    
    suscripcion = Suscripcion.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(suscripcion, 20)
        suscripcion = paginator.page(page)
    except:
        raise Http404
    data = {
        'suscripcionCliente': suscripcion,
        'paginator': paginator
    }
    return render(request, 'core/crud/listar_suscripcion.html', data)

@login_required(login_url='/login/')
@permission_required('is_staff')
def agregar_suscripciones(request):
    data = {
        'form': SuscripcionForm()
    }
    if(request.method == "POST"):
        formulario = SuscripcionForm(data=request.POST, files=request.FILES)
        if(formulario.is_valid()):
            formulario.save() 
            messages.success(request, "Suscripcion registrada correctamente")
            return redirect('/mi_cuenta_CRUD')
        else:
            messages.error(request, "No se ha podido agregar la suscripcion, intente nuevamente")
            data["form"] = formulario
    return render(request, 'core/crud/agregar_suscripcion.html', data)

@login_required(login_url='/login/')
@permission_required('is_staff')
def modificar_suscripciones(request, id):
    suscripcion = get_object_or_404(Suscripcion, id=id)
    data = {
        'form':SuscripcionForm(instance=suscripcion)
    }
    if(request.method == 'POST'):
        formulario = SuscripcionForm(data=request.POST, instance=suscripcion)
        if(formulario.is_valid()):
            formulario.save()
            messages.success(request, "Suscripcion modificada correctamente" )
            return redirect('/listar_suscripciones')
        else:
            messages.error(request, "La suscripcion no se ha podido modificar" )
            data['form'] = formulario
    return render(request, 'core/crud/modificar_suscripcion.html', data)

@login_required(login_url='/login/')
@permission_required('is_staff')
def eliminar_suscripciones(request, id):
    suscripcion = get_object_or_404(Suscripcion, id=id)
    try:
        suscripcion.delete()
        messages.success(request, "Suscripcion eliminada exitosamente")
    except:
        messages.error(request, "La suscripcion no se ha podido eliminar")
    return redirect('/listar_suscripciones')


    
