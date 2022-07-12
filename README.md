Proyecto_Pet_Examen
Proyecto examen

PROYECTO EXAMEN GRUPO 3 - DUOC UC Fundación PET - Caso Forma A

///--------------------------------------------------------------------------------------------------------------------------/// Proyecto realizado con Python, Django y Django Rest Base de Datos Oracle 19c

Revisado en Navegador Chrome, Opera, Edge funcionando correctamente

En Firefox (ultima version) funciona pero existe un problema de Eventos del Mouse Element.setCapture() que no despliega el boton de agregar productos en tienda.

///--------------------------------------------------------------------------------------------------------------------------///

Caracteristicas
Registrar usuarios (sin privilegios de administrador)
Registrar, Listar, Modificar, Eliminar productos (Solo disponible con superusuario ADMIN)
Registrar, Listar, Modificar, Eliminar adopciones (Solo disponible con superusuario ADMIN)
Listar, Modificar, Eliminar suscripciones (Solo disponible con superusuario ADMIN)
Authenticacion y autorizacion por Token (Al registrar/loguearse crea token... al cerrar sesion destruye token)
Mostrar productos en Tienda (requiere login)
Agregar, eliminar, limpiar productos de carro de compras, lista de deseo, comparador productos.
Suma, resta, elimina cantidades de productos del carrito.
Panel de Usuario con opcion de suscripcion.
Carrito de compras
Api externa del Clima funcional, accediendo directamente desde Slider del home.
Api de geolocalizacion de Google en nosotros y contacto
Consumo de Api propia Django Rest API
#Lo que no hace

No genere orden de compra
No tiene proceso de pago
Despacho de productos (Solo esta maquetado)
No modifica informacion del usuario
No aplica descuento por usuario suscrito. ///--------------------------------------------------------------------------------------------------------------------------///
Porfavor leer antes de iniciar aplicación.

Inicie el programa VsCode e intale el requirements.txt de la siguiente forma, en el terminal ingrese:

pip install -r requirements.txt
Inicie SQLPLUS con su usuario y contraseña e ingrese la siguiente configuración:

alter session set "_ORACLE_SCRIPT" = True;
create user c##grupo3 identified by grupo3;
grant connect, resource to c##grupo3;
alter user c##grupo3 default tablespace users quota unlimited on users;
En la terminal de VSCOde, ejecute los siguientes comandos:

makemigrations = "python manage.py makemigrations" migrate = "python manage.py migrate" createsuperuser = "python manage.py createsuperuser" server = "python manage.py runserver"

Ejecute en SQL Developer Oracle el Script :

SCRIPT_Poblado de tablas.sql para cargar los datos en tablas de la aplicacion.
--Como administrador (superusuario) Puede agregar productos Puede agregar adopciones

Las fotografias a cargar para estas pruebas se encuentran en la raiz del proyecto como carpeta Imagenes_Prueba Agregar (possen un tamaño especifico para no deformar el cart.

Consumo de Api propia Django Rest API
Acceso a Ruta de las Api con ViewSet (Comprobar Autorizacion con Token desde la web)
  http://127.0.0.1:8000/api/rest_api/

-Acceso a Ruta de las Api con API VIEW (Comprobar con Authorization Token)

  http://127.0.0.1:8000/api/lista_usuarios
  http://127.0.0.1:8000/api/detalle_usuarios/<id>
  http://127.0.0.1:8000/api/lista_productos
  http://127.0.0.1:8000/api/detalle_productos/<id>
  http://127.0.0.1:8000/api/lista_adopciones
  http://127.0.0.1:8000/api/detalle_adopciones/<id>
  http://127.0.0.1:8000/api/lista_marcas
  http://127.0.0.1:8000/api/detalle_marcas/<id>
PARA CONSULTAS SQL EN BASE DE DATOS SE PROPORCIONAN LAS SIGUIENTES CONSULTAS.

--Eliminar los contenidos de las tablas delete from auth_user; delete from authtoken_token; delete from core_adopcion; delete from core_contacto1; delete from core_contactoadopcion; delete from core_marca; delete from core_persona; delete from core_producto; delete from core_suscripcion; delete from weather_city;

Commit;

--Consuta de las tablas del modelo select * from auth_user; select * from authtoken_token; select * from core_adopcion; select * from core_contacto1; select * from core_contactoadopcion; select * from core_marca; select * from core_persona; select * from core_producto; select * from core_suscripcion; select * from weather_city;

--Consulta para obtener el usuario que tiene generado un TOKEN al Loguearse o registrarse en la APP --Se destruye cuando cierra sesion y se desloguea select au.id,au.username, au.email,at.key, au.password from auth_user au join authtoken_token at on au.id = at.user_id;

--Consulta para eliminar registro en BDA excepto del admin delete from auth_user where username != 'admin'; commit;
