from abc import ABC, abstractmethod


class Creature(ABC):
    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def make_noise(self):
        pass


class Animal(Creature):
    def feed(self):
        print("Питается травой")

    def move(self):
        print("Медлительный")

    def make_noise(self):
        print("Издает звук - 'МУУУУУУ'")


# Абстрактный декоратор, от которого будут наследоваться все другие
class Decorator(Creature):
    def __init__(self, obj):
        self.obj = obj

    def feed(self):
        self.obj.feed()

    def move(self):
        self.obj.move()

    def make_noise(self):
        self.obj.make_noise()


class Swimming(Decorator):
    def move(self):
        print("Плавает")

    def make_noise(self):
        print("...")


class Flying(Decorator):
    def move(self):
        print("Летает")

    def make_noise(self):
        print("...")


class Predator(Decorator):
    def feed(self):
        print("Питается мясом")


class Fast(Decorator):
    def move(self):
        self.obj.move()
        print("Быстрый")


animal = Animal()
animal.feed()
animal.move()
animal.make_noise()
print()

animal = Swimming(animal)
animal.feed()
animal.move()
animal.make_noise()
print()

animal = Predator(animal)
animal.feed()
animal.move()
animal.make_noise()
print()

animal = Fast(animal)
animal.feed()
animal.move()
animal.make_noise()
print()

animal = Flying(animal)
animal.feed()
animal.move()
animal.make_noise()
print()
