import random
from court import Court
from player import Team

class Match():

    def __init__(self):
        self.__set1 = 0
        self.__set2 = 0

    @property
    def set1(self):
        return self.__set1
    
    @set1.setter
    def set1(self, set1):
        self.__set1 = set1
    
    @property
    def set2(self):
        return self.__set2
    
    @set2.setter
    def set2(self, set2):
        self.__set2 = set2

    def simulate_match(self):
        while self.set1 < 4 and self.set2 < 4:
            self.simulate_set()

    def __shot(self):
        random.seed()
        return random.randint(0,1)

    def simulate_set(self):
        points1 = 0
        points2 = 0
        
        while points1 <= 40 and points2 <= 40:
            if self.__shot() == 0:
                points1 += 15
                print("Puntos del equipo 1: ", points1)
            elif self.__shot() == 1:
                points2 += 15
                print("Puntos del equipo 2: ", points2)
        
        if points1 == 45:
            print("Ganó el equipo 1")
            self.set1 += 1
        else:
            print("Ganó el equipo 2")
            self.set2 += 1


class Game():
    def __init__(self, court:Court, team1:Team, team2:Team):
        self.__court = court
        self.__team1 = team1
        self.__team2 = team2   
    
    @property
    def team1(self):
        return self.__team1
    
    @team1.setter
    def team1(self, team1):
        self.__team1 = team1
    
    @property
    def team2(self):
        return self.__team2
    
    @team2.setter
    def team2(self, team2):
        self.__team2 = team2

    def __str__(self):
        return f"{self.name_court}, {self.team1}, {self.team2}"
    
    def assign_court(self, court):
        self.__court = court
    
    def assign(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def play(self):
        match = Match()
        match.simulate_match()
        if match.set1 == 4:
            print("Victoria del equipo 1", self.team1)
        else:
            print("Victoria del equipo 2", self.team2)