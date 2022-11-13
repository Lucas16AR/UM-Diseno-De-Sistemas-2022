from abc import ABC, abstractmethod
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


class Command(ABC):
    
    @abstractmethod
    def execute(self):
        pass        

class Compra(Command):
    def execute(self, producto):
        print("Validando producto", producto.nombre)


class Correo(Command):
    def execute(self, producto):
        print("Usted compro ", producto.nombre)


class Factura(Command):
    def execute(self, producto):
        print("Factura de compra por ", producto.nombre," por un valor de ", producto.importe)


class Despacho(Command):
    def execute(self, producto):
        print ("Su producto ", producto.nombre, " esta en camino")


class Seguimiento(Command):
    def execute(self, producto):
        print ("Tu codigo de seguimiento es ", random.randint(1,1000), " para el producto", producto.nombre)

class Ranking(Command):
    def __valorar(self, producto):
        print("valorando ", producto.nombre)

    def execute(self, producto):
        self.__valorar(producto)

class Invoker():

    def __init__(self):
        self.__tareas = []
        
    def add_tarea(self, tarea: Command):
        self.__tareas.append(tarea)

    def execute(self, producto):
        for tarea in self.__tareas:
            tarea.execute(producto)

class Cliente(Command):
    def execute(self, producto):
        invoker = Invoker()
        invoker.add_tarea(Compra())

        invoker.add_tarea(Correo())

        invoker.add_tarea(Despacho())

        invoker.add_tarea(Seguimiento())

        invoker.execute(producto)

if __name__ == "__main__":
    producto = Producto("i9 13900k", 800)
    cliente = Cliente()
    cliente.execute(producto)
