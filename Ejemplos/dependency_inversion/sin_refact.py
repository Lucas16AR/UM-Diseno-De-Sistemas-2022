class Engine(object):
    
    def __init__(self):
        pass

    def accelerate(self):
        pass

    def rpm(self):
        currentRPM = 0
        return currentRPM

class Vehicle(object):

    def __init__(self):
        self._engine = Engine()

    def getEngineRPM(self):
        return self._engine.rpm()