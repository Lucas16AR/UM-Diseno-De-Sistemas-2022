from abc import ABC, abstractmethod
from random import randrange
from threading import Thread
import time
from colorama import Fore, init
init(autoreset=True)


class Subject(ABC):
    @abstractmethod
    def attach(self, observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer) -> None:
        pass

    @abstractmethod
    def notify(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, observable, object):
        pass

class ConcreteSubject(Thread,Subject):
    _state = None
    _observers = []

    def __init__(self, *args, **kwargs): #Setear mas cantidad de patrones, no hace falta establecerlas antes.
        Thread.__init__(self, *args, **kwargs)
        self._finish = False

    def run(self) -> None:
        while not self._finish:
            self.logica_de_negocio()
            time.sleep(1)
    
    def attach(self, observer: Observer):
        print(Fore.RED + "Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer):
        print(Fore.CYAN + "Subject: Detached an observer.")
        self._observers.remove(observer)

    def notify(self) -> None:
        print(Fore.RED + "Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def stop(self):
        self._finish = True
    
    def logica_de_negocio(self) -> None:
        print(Fore.GREEN + "Subject: I'm doing something important.")
        self._state = randrange(0, 10)
        self.notify()


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 5:
            print(Fore.GREEN + "ConcreteObserverA: Reacted to the event")

class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state > 5:
            print(Fore.YELLOW + "ConcreteObserverB: Reacted to the event")

class ConcreteObserverC(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print(Fore.BLUE + "ConcreteObserverC: Reacted to the event")

if __name__ == "__main__":
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    observer_c = ConcreteObserverC()
    subject.attach(observer_c)

    subject.start()
    time.sleep(3)
    subject.stop()
    subject.join()