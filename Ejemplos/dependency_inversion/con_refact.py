class Engine(object):
    
    def __init__(self):
        pass

    def accelerate(self):
        pass

    def rpm(self):
        currentRPM = 0
        return currentRPM

class Vehicle(object):

    def __init__(self, engine):
        self._engine = engine

    def getEngineRPM(self):
        return self._engine.rpm()

if __name__ == '__main__':
    vehicle = Vehicle(Engine())
    print(vehicle.getEngineRPM())