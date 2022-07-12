# from django.conf.urls import url
# from django.conf import settings
# from django.views.static import serve
from django.urls import path
from .views import index,blog,carro,checkout,compare,error_404,\
                    galeria,nosotros,\
                    wishlist,tiendafor,contacto1,listar_producto,agregar_producto,\
                    modificar_producto,eliminar_producto,registro_usuario,mi_cuenta,\
                    mi_cuenta_CRUD,adopcion_mascota,listar_mascota,agregar_mascota,\
                    modificar_mascota,eliminar_mascota,contacto_adopcion,agregar_suscripcion,\
                    listar_suscripciones,agregar_suscripciones,modificar_suscripciones,eliminar_suscripciones,order

urlpatterns = [
    path('', index, name="index"),
    path('adopcion_mascota/', adopcion_mascota, name="adopcion_mascota"),
    path('contacto_adopcion/', contacto_adopcion, name="contacto_adopcion"),
    path('error_404/', error_404, name="error_404"),
    path('galeria/', galeria, name="galeria"),
    path('nosotros/', nosotros, name="nosotros"),
    path('tiendafor/', tiendafor, name="tiendafor"),
    path('contacto1/', contacto1, name="contacto1"),
    path('blog/', blog, name="blog"),
    
    path('registro_usuario/', registro_usuario, name="registro_usuario"),
    path('mi_cuenta/', mi_cuenta, name="mi_cuenta"),
    path('mi_cuenta_CRUD/', mi_cuenta_CRUD, name="mi_cuenta_CRUD"),

    path('carro/', carro, name="carro"),
    path('checkout/', checkout, name="checkout"),
    path('compare/', compare, name="compare"),
    path('wishlist/', wishlist, name="wishlist"),

    path('listar_producto/', listar_producto, name="listar_producto"),
    path('agregar_producto/', agregar_producto, name="agregar_producto"),
    path('modificar_producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<id>/', eliminar_producto, name="eliminar_producto"),
 
    path('listar_mascota/', listar_mascota, name="listar_mascota"),
    path('agregar_mascota/', agregar_mascota, name="agregar_mascota"),
    path('modificar_mascota/<id>/', modificar_mascota, name="modificar_mascota"),
    path('eliminar_mascota/<id>/', eliminar_mascota, name="eliminar_mascota"),

    path('agregar_suscripcion/', agregar_suscripcion, name="agregar_suscripcion"),

    path('listar_suscripciones/', listar_suscripciones, name="listar_suscripciones"),
    path('agregar_suscripciones/', agregar_suscripciones, name="agregar_suscripciones"),
    path('modificar_suscripciones/<id>/', modificar_suscripciones, name="modificar_suscripciones"),
    path('eliminar_suscripciones/<id>/', eliminar_suscripciones, name="eliminar_suscripciones"),

    path('order/', order, name="order"),




]