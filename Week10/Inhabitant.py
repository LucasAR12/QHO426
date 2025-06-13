from abc import ABC

class Inhabitant(ABC):
    MAX_ENERGY = 100

    def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY):
        self.name = name
        self.age = age
        self.energy = energy

    def eat(self, amount):
        self.energy = min(self.energy + amount, Inhabitant.MAX_ENERGY)

    def grow(self):
        self.age += 1

    def move(self, distance):
        if self.energy >= distance:
            self.energy -= distance

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', age={self.age}, energy={self.energy})"

    def __str__(self):
        return f"{self.name}, Age: {self.age}, Energy: {self.energy}"
