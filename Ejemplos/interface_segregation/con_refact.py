class BirdNew:
    def walk(self):
        return 'I can walk'

class BirdEat(BirdNew):
    def eat(self):
        return 'I can eat'

class PenguinNew(BirdNew):
    def walk(self):
        return super().walk()

class Duck(BirdEat):
    def fly(self):
        return super().eat()