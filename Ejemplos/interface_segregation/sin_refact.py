class Bird:
    def fly(self):
        print("Can fly")

    def eat(self):
        print("Can Eat")

class Penguin:
    def fly(self):
        raise NotImplementedError("Can't fly")