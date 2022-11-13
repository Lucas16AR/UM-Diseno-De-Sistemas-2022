class Autenticacion():
    def user(self):
        print ("ingresar usuario")

    def pdw(self):
        print("ingresar contraseña")
    
    def obtener(self):
        print("obtener")

class Caja ():
    def saldo(self):
        print ("saldo")
    
    def obtener_dinero (self):
        print ("obtener dinero")

    def debitar_dinero(self):
        print ("debitar dinero")

class ModoFacade ():
    
    def __init__(self):
        self.__autenticacion = Autenticacion()
        self.__caja = Caja()   
    
    def todo(self):
        self.__autenticacion.user()
        self.__autenticacion.pdw()
        self.__autenticacion.obtener()

        self.__caja.saldo()
        self.__caja.obtener_dinero()
        self.__caja.debitar_dinero()

class Cliente():
    def __init__(self, facade:ModoFacade):
        self.__facade = facade
    
    def execute(self):
        self.__facade.todo()

if __name__ == "__main__":
    facade = ModoFacade()
    cliente = Cliente(facade)
    cliente.execute()
