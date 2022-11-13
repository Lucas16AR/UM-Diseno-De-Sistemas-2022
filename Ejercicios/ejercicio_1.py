class Venta():

    def __init__(self, vendedor) -> None:
        self.__productos = []
        self.__vendedor = vendedor
        self.__precio_total = 0
        self.__comision = 0

    @property
    def vendedor(self):
        return self.__vendedor

    @vendedor.setter
    def vendedor(self, vendedor):
        self.__vendedor = vendedor

    @property
    def precio_total(self):
        return self.__precio_total

    @precio_total.setter
    def precio_total(self, precio_total):
        self.__precio_total = precio_total

    @property
    def comision(self):
        return self.__comision

    @comision.setter
    def comision(self, comision):
        self.__comision

    def agregar_producto(self, producto, cantidad):
        self.__productos.append(producto)
        self.__precio_total += producto.precio * cantidad

    def calcular(self):
        if self.__precio_total <= 500:
            self.__comision = self.__calcular_comision(0)
        elif 500 < self.__precio_total <= 1000:
            self.__comision = self.__calcular_comision(10)
        elif 1000 < self.__precio_total <= 1500:
            self.__comision = self.__calcular_comision(25)
        elif self.__precio_total > 1500:
            self.__comision = self.__calcular_comision(35)

    def __calcular_comision(self, porcentaje):
        return (self.__precio_total * porcentaje) / 100
        
class Vendedor():

    def __init__(self, nombre) -> None:
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

class Producto():

    def __init__(self, nombre, precio, codigo) -> None:
        self.__nombre = nombre
        self.__precio = precio
        self.__codigo = codigo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio: float):
        if precio < 0:
            print("No se puede ingresar valores negativos.")    
        self.__precio = abs(precio)
    
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: str):
        self.__nombre = codigo

def main():
    producto = Producto("Memoria RAM", 200, "ram-16")
    producto.precio = -200
    producto2 = Producto("Procesador Ryzen", 700, "ryzen-3600")
    producto3 = Producto("Motherboard", 500, "b450m")
    vendedor = Vendedor("Nicolas")
    pedido = Venta(vendedor)
    pedido.agregar_producto(producto, 2)
    pedido.agregar_producto(producto2, 1)
    pedido.agregar_producto(producto3, 1)
    pedido.calcular()
    print(f"El precio total es: {pedido.precio_total} y {pedido.comision} de comision del vendedor {pedido.vendedor.nombre}.")

if __name__ == '__main__':
    main()