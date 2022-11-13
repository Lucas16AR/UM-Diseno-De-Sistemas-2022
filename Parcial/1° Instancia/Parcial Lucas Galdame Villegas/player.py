class Player():
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return f'{self.__name}'


class Team():
    def __init__(self, player1, player2):
        self.__player1 = player1
        self.__player2 = player2

    def __str__(self):
        return f'{self.__player1.name} y {self.__player2.name}'