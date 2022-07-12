from django.urls import path, include
from rest_api.viewslogin import login
from rest_framework import routers
from core.views import index
from rest_api.views import lista_productos, detalle_productos,lista_adopciones,detalle_adopciones,\
 ProductoViewset,MarcaViewset, AdopcionViewset,PersonaViewset,UsuarioViewset, lista_usuarios,detalle_usuarios,\
lista_marcas,detalle_marcas
from rest_framework.authtoken import views

#Importar de VIEWS a PersonaList
from .views import PersonaList

### Accede a las vistas desde http://127.0.0.1:8000/api/rest_api/
### Estas vistas no son visibles con Token de Autenticacion mediante el ADVANCE REST CLIENT DE CHROME
router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('marca', MarcaViewset)
router.register('adopcion', AdopcionViewset)
router.register('persona', PersonaViewset)
router.register('usuario', UsuarioViewset)



urlpatterns = [
    path('lista_marcas', lista_marcas, name="lista_marcas"),
    path('detalle_marcas/<id>', detalle_marcas, name="detalle_marcas"),

    path('lista_usuarios', lista_usuarios, name="lista_usuarios"),
    path('detalle_usuarios/<id>', detalle_usuarios, name="detalle_usuarios"),

    path('lista_productos', lista_productos, name="lista_productos"),
    path('detalle_productos/<id>', detalle_productos, name="detalle_productos"),

    path('lista_adopciones', lista_adopciones, name="lista_adopciones"),
    path('detalle_adopciones/<id>', detalle_adopciones, name="detalle_adopciones"),

    #path('login', login, name="login"),

    path('rest_api/', include (router.urls)),
    path('api_generate_token', views.obtain_auth_token),

    #Es una VISTA basada en CLASE
    path('persona/', PersonaList.as_view(), name='persona_list'),
    
    path('', index, name="index"),

    
    

]

