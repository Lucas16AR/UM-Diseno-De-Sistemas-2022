import random

class Jugador():
    def __init__(self,name):
        self.__name = name

    def eleccion(self, elegido):
        self.__elegido = elegido

    def obtener_seleccion(self):
        return self.__elegido

    def obtener_nombre(self):
        return self.__name

class Juego():
    def crear_jugador(self):
        self.__jugador1 = Jugador("Santiago")
        self.__jugador2 = Jugador("Bruno")
        self.__elecciones = ['Piedra', 'Papel', 'Tijera']

    def jugar(self):
        self.__jugador1.eleccion(self.__elegir())
        self.__jugador2.eleccion(self.__elegir())
        if self.__jugador1.obtener_seleccion() == self.__jugador2.obtener_seleccion():
            print("Empate")
        elif self.__jugador1.obtener_seleccion() == "Tijera":
            if self.__jugador2.obtener_seleccion() == "Papel":
               self.__mostrar(self.__jugador1)
            else: 
               self.__mostrar(self.__jugador2)
        elif self.__jugador1.obtener_seleccion() == "Piedra":
            if self.__jugador2.obtener_seleccion() == "Tijera":
               self.__mostrar(self.__jugador1)
            else:
               self.__mostrar(self.__jugador2)
        
        elif self.__jugador1.obtener_seleccion() == "Papel":
            if self.__jugador2.obtener_seleccion() == "Piedra":
               self.__mostrar(self.__jugador1)
            else:
               self.__mostrar(self.__jugador2)
        
        print("Ronda Terminada")

    def __mostrar(self,jugador):
        print(f'gano {jugador.obtener_nombre()} con {jugador.obtener_seleccion()}')

    def __elegir(self):
        random.seed()
        return random.choice(self.__elecciones)

if __name__ ==  "__main__":
    juego = Juego()
    juego.crear_jugador()
    juego.jugar()