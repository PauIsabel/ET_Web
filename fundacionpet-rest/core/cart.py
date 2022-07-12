from .models import Producto

class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            self.session["cart"] = {}
            self.cart = self.session["cart"]
        else:
            self.cart = cart

    def agregar(self, producto):
        if str(producto.id) not in self.cart.keys():
            self.cart[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "precio_oferta": producto.precio_oferta,
                "stock": producto.stock,
                "descripcion": producto.descripcion,
                
                "imagen": producto.imagen.url,
                "cantidad": 1,
                "acumulado": producto.precio_oferta,                                
            }
        else:
            for key, value in self.cart.items():
                if key == str(producto.id):
                    value["cantidad"] = value ["cantidad"] + 1
                    value["acumulado"] += producto.precio_oferta                    
                    break
        self.save()

    def agregar2(self, producto):
        if str(producto.id) not in self.cart.keys():
            self.cart[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "precio_oferta": producto.precio_oferta,
                "stock": producto.stock,
                "descripcion": producto.descripcion,
                
                "imagen": producto.imagen.url,
                "cantidad": 1,
                "acumulado": producto.precio_oferta,                                
            }
        else:
            for key, value in self.cart.items():
                if key == str(producto.id):
                    value["cantidad"] = value ["cantidad"] + 1
                    value["acumulado"] += producto.precio_oferta                    
                    break
        self.save()

#METODO SAVE PARA GUARDAR PRODUCTO AL CARRITO
    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True


#METODO REMOVE PARA REMOVER PRODUCTO AL CARRITO
    def eliminar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()


#METODO DECREMENT PARA RESTAR PRODUCTO AL CARRITO
    def restar(self, producto):
        for key, value in self.cart.items():
            if key == str(producto.id):
                value["cantidad"] = value ["cantidad"] - 1
                value["acumulado"] -= producto.precio_oferta
                if value["cantidad"] <1:
                    self.eliminar(producto)
                else:
                    self.save()
                break
            else:
                print("El producto no existe en el carrito")


#METODO CLEAR PARA LIMPIAR EL CARRITO
    def limpiar(self):
        self.session["cart"] = {}
        self.session.modified =True





#METODO CLASE WISHLIST#METODO CLASE WISHLIST#METODO CLASE WISHLIST
class Wishlist:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        wish = self.session.get("wish")
        if not wish:
            self.session["wish"] = {}
            self.wish = self.session["wish"]
        else:
            self.wish = wish

    def agregarW(self, producto):
        if str(producto.id) not in self.wish.keys():
            self.wish[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "precio_oferta": producto.precio_oferta,
                "stock": producto.stock,
                "descripcion": producto.descripcion,               
                "imagen": producto.imagen.url,
                "cantidad": 1,
                "acumulado": producto.precio_oferta,                                
            }
        else:
            for key, value in self.wish.items():
                if key == str(producto.id):
                    value["cantidad"] = value ["cantidad"] + 1
                    value["acumulado"] += producto.precio_oferta                    
                    break
        self.save()

    def agregarW2(self, producto):
        if str(producto.id) not in self.wish.keys():
            self.wish[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "precio_oferta": producto.precio_oferta,
                "stock": producto.stock,
                "descripcion": producto.descripcion,               
                "imagen": producto.imagen.url,
                "cantidad": 1,
                "acumulado": producto.precio_oferta,                                
            }
        else:
            for key, value in self.wish.items():
                if key == str(producto.id):
                    value["cantidad"] = value ["cantidad"] + 1
                    value["acumulado"] += producto.precio_oferta                    
                    break
        self.save()

#METODO SAVE PARA GUARDAR PRODUCTO AL WISHLIST
    def save(self):
        self.session["wish"] = self.wish
        self.session.modified = True


#METODO REMOVE PARA REMOVER PRODUCTO AL WISHLIST
    def eliminarW(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.wish:
            del self.wish[producto_id]
            self.save()


#METODO DECREMENT PARA RESTAR PRODUCTO AL WISHLIST
    def restarW(self, producto):
        for key, value in self.wish.items():
            if key == str(producto.id):
                value["cantidad"] = value ["cantidad"] - 1
                value["acumulado"] -= producto.precio_oferta
                if value["cantidad"] <1:
                    self.eliminarW(producto)
                else:
                    self.save()
                break
            else:
                print("El producto no existe en el carrito")


#METODO CLEAR PARA LIMPIAR EL WISHLIST
    def limpiarW(self):
        self.session["wish"] = {}
        self.session.modified =True




#METODO CLASE COMPARADOR#METODO CLASE COMPARADOR#METODO CLASE COMPARADOR#METODO CLASE COMPARADOR
class Compare:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        compare = self.session.get("compare")
        if not compare:
            self.session["compare"] = {}
            self.compare = self.session["compare"]
        else:
            self.compare = compare


    def agregarC(self, producto):
        if str(producto.id) not in self.compare.keys():
            self.compare[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "precio_oferta": producto.precio_oferta,
                "stock": producto.stock,
                "descripcion": producto.descripcion,
                
                "imagen": producto.imagen.url,
                "cantidad": 1,
                "acumulado": producto.precio_oferta,                                
            }
        else:
            for key, value in self.compare.items():
                if key == str(producto.id):
                    value["cantidad"] = value ["cantidad"] + 1
                    value["acumulado"] += producto.precio_oferta                    
                    break
        self.save()

    def agregarC2(self, producto):
        if str(producto.id) not in self.compare.keys():
            self.compare[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "precio_oferta": producto.precio_oferta,
                "stock": producto.stock,
                "descripcion": producto.descripcion,
                
                "imagen": producto.imagen.url,
                "cantidad": 1,
                "acumulado": producto.precio_oferta,                                
            }
        else:
            for key, value in self.compare.items():
                if key == str(producto.id):
                    value["cantidad"] = value ["cantidad"] + 1
                    value["acumulado"] += producto.precio_oferta                    
                    break
        self.save()



#METODO SAVE PARA GUARDAR PRODUCTO AL COMPARADOR
    def save(self):
        self.session["compare"] = self.compare
        self.session.modified = True


#METODO REMOVE PARA REMOVER PRODUCTO AL COMPARADOR
    def eliminarC(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.compare:
            del self.compare[producto_id]
            self.save()


#METODO DECREMENT PARA RESTAR PRODUCTO AL COMPARADOR
    def restarC(self, producto):
        for key, value in self.compare.items():
            if key == str(producto.id):
                value["cantidad"] = value ["cantidad"] - 1
                value["acumulado"] -= producto.precio_oferta
                if value["cantidad"] <1:
                    self.eliminarC(producto)
                else:
                    self.save()
                break
            else:
                print("El producto no existe en el carrito")


#METODO CLEAR PARA LIMPIAR EL COMPARADOR
    def limpiarC(self):
        self.session["compare"] = {}
        self.session.modified =True