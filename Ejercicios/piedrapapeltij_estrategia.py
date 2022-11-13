from abc import ABC, abstractmethod
import random 

class Strategy(ABC):
    @abstractmethod
    def obtener_seleccion(self):
        pass

class Piedra(Strategy):
    def obtener_seleccion(self):
        return "Piedra"

class Papel(Strategy):
    def obtener_seleccion(self):
        return "Papel"

class Tijera(Strategy):
    def obtener_seleccion(self):
        return "Tijera"

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
    def __init__(self, strategy):
        self.__strategy = strategy

    def crear_jugador(self):
        self.__strategy = Jugador("Santiago")
        jugador2 = Jugador("Bruno")
        self.__elecciones = ['Piedra', 'Papel', 'Tijera']

    def jugar(self, jugador2):
        jugador2.eleccion(self.__elegir())
        if self.__strategy.obtener_seleccion() == jugador2.obtener_seleccion():
            print("Empate")
        elif self.__strategy.obtener_seleccion() == "Tijera":
            if jugador2.obtener_seleccion() == "Papel":
               self.__mostrar(self.__strategy)
            else: 
               self.__mostrar(jugador2)
        elif self.__strategy.obtener_seleccion() == "Piedra":
            if jugador2.obtener_seleccion() == "Tijera":
               self.__mostrar(self.__strategy)
            else:
               self.__mostrar(jugador2)
        
        elif self.__strategy.obtener_seleccion() == "Papel":
            if jugador2.obtener_seleccion() == "Piedra":
               self.__mostrar(self.__strategy)
            else:
               self.__mostrar(jugador2)
        
        print("Ronda Terminada")

    def __mostrar(self,jugador):
        print(f'gano {jugador.obtener_nombre()} con {jugador.obtener_seleccion()}')

    def __elegir(self):
        random.seed()
        return random.choice(self.__elecciones)