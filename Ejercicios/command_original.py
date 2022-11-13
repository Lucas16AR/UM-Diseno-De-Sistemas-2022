import random
class Producto():
    def __init__(self, nombre, importe):
        self.__nombre = nombre
        self.__importe = importe
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def importe(self):
        return self.__importe

    @importe.setter
    def importe(self, importe):
        self.__importe = importe
        
class Compra():
    def validar(self, producto):
        print("Validando producto", producto.nombre)


class Correo():
    def enviar_email(self, producto):
        print("Usted compro ", producto.nombre)


class Factura():
    def factura(self, producto):
        print("Factura de compra por ", producto.nombre," por un valor de ", producto.importe)


class Despacho():
    def transporte(self, producto):
        print ("Su producto ", producto.nombre, " esta en camino")


class Seguimiento():
    def codigo(self, producto):
        print ("Tu codigo de seguimiento es ", random.randint(1,1000), " para el producto", producto.nombre)

class Ranking():
    def valorar(self, producto):
        print("valorando ", producto.nombre)

if __name__ == "__main__":
    producto = Producto("i9 13900k", 800)
    
    compra = Compra()
    compra.validar(producto)

    correo = Correo()
    correo.enviar_email(producto)

    despacho = Despacho()
    despacho.transporte(producto)

    factura = Factura()
    factura.factura(producto)

    seguimiento = Seguimiento()
    seguimiento.codigo(producto)

    ranking = Ranking()
    ranking.valorar(producto)
