from Inhabitant import Inhabitant

class Robot(Inhabitant):
    laws = [
        "A robot may not injure a human being or, through inaction, allow a human being to come to harm.",
        "A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.",
        "A robot must protect its own existence as long as such protection does not conflict with the First or Second Law."
    ]

    def __init__(self, name="Robot", age=0, energy=Inhabitant.MAX_ENERGY):
        super().__init__(name, age, energy)

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        return super().__str__()

    def display(self):
        print(self)

    @staticmethod
    def the_laws():
        return Robot.laws
