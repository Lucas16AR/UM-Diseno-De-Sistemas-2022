"""
Programar en Python las siguientes clases:
a) Jugador, Cancha de Paddle con atributos como:
• Nombre de la cancha
• Equipo A y Equipo B constituido por 2 jugadores por equipo

b) Escribir por lo menos un método para crear jugadores, cancha y asignar las parejas de
paddle que competiran.

c) Simular un partido de Paddle, el cual se divide en sets. Cada set es ganado cuando uno de
los equipos llega a 45 puntos (El primer punto que gana una pareja suma 15 puntos; el
segundo, 30; el cuarto, 45), el cual se reinicia cada nuevo set. Los equipos alternaran
turnos de saque que podrán ganar o no. Tras ganar un set debe mostrar el nombre de los
jugadores que ganaron el Set e incrementarse el total de set ganados. Cuando un equipo
llega a 4 Set ganados se termina el juego.

d) Al final se mostrarán los jugadores de cada equipo, nombre de la cancha , total de set
ganados por equipo y equipo ganador.
"""

from abc import ABC, abstractmethod
import random


class Jugador(ABC):
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    def __repr__(self):
        return "({} {})".format(self.__nombre, self.__apellido)

    
class Cancha():
    def __init__(self, nombre, equipoA, equipoB):
        self.__nombre = nombre
        self.__equipoA = [equipoA[0], equipoA[1]]
        self.__equipoB = [equipoB[0], equipoB[1]]
    
    @property
    def nombre_cancha(self):
        return self.__nombre
    
    @nombre_cancha.setter
    def nombre_cancha(self, nombre):
        self.__nombre = nombre
    
    @property
    def equipoA(self) -> None:
        return self.__equipoA
    
    @equipoA.setter
    def equipoA(self, equipoA) -> None:
        self.__equipoA = equipoA
    
    @property
    def equipoB(self) ->None:
        return self.__equipoB
    
    @equipoB.setter
    def equipoB(self, equipoB) -> None:
        self.__equipoB = equipoB

    def __repr__(self):
        return "({} {} {})".format(self.nombre_cancha, self.equipoA, self.equipoB)


class Paddle(Cancha):
    def __init__(self, nombre, equipoA, equipoB):
        super().__init__(nombre, equipoA, equipoB)
        self.__setA = 0
        self.__setB = 0
    
    @property
    def setA(self):
        return self.__setA
    
    @setA.setter
    def setA(self, setA):
        self.__setA = setA
    
    @property
    def setB(self):
        return self.__setB
    
    @setB.setter
    def setB(self, setB):
        self.__setB = setB
    
    def crear_jugador(self, nombre, apellido):
        jugador = Jugador(nombre, apellido)
        return jugador
    
    def crear_cancha(self, nombre, equipoA, equipoB):
        cancha = Paddle(nombre, equipoA, equipoB)
        return cancha
    
    def asignar_parejas(self, equipoA, equipoB):
        self.equipoA = equipoA
        self.equipoB = equipoB
    
    def simular_partido(self):
        while self.setA < 4 and self.setB < 4:
            self.simular_set()
        if self.setA == 4:
            print("Ganó el partido el equipo A \n Felicitaciones: \n", self.equipoA)
            print("Nombre de la cancha: \n", self.nombre_cancha)
        else:
            print("Ganó el partido el equipo B \n Felicitaciones: \n", self.equipoB)
            print("Nombre de la cancha: \n", self.nombre_cancha)

    def simular_set(self):
        puntosA = 0
        puntosB = 0
        while puntosA < 45 and puntosB < 45:
            puntosA += self.simular_saque()
            puntosB += self.simular_saque()
            print("Puntos equipo A: ", puntosA)
            print("Puntos equipo B: ", puntosB)
        if puntosA == 45:
            print("Ganó el equipo A")
            self.setA += 1
        else:
            print("Ganó el equipo B")
            self.setB += 1
    
    def simular_saque(self):
        return random.randint(0, 1) * 15


def main():
    jugador1 = Jugador("Juan", "Riquelme")
    jugador2 = Jugador("Fernando", "Gago")
    jugador3 = Jugador("Pipa", "Benedetto")
    jugador4 = Jugador("Agustin", "Rossi")
    equipoA = [jugador1, jugador3]
    equipoB = [jugador2, jugador4]
    cancha = Paddle("La Bombonera", equipoA, equipoB)
    cancha.simular_partido()

if __name__ == "__main__":
    main()