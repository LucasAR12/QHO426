from Inhabitant import Inhabitant

class Human(Inhabitant):
    def __init__(self, name="Human", age=0, energy=Inhabitant.MAX_ENERGY):
        super().__init__(name, age, energy)

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        return super().__str__()

    def display(self):
        print(self)
