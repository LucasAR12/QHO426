from human import Human

from robot import Robot

class Planet:
    def __init__(self, name):
        self.name = name
        self.inhabitants = []

    def add_inhabitant(self, inhabitant):
        if inhabitant not in self.inhabitants:
            self.inhabitants.append(inhabitant)

    def remove_inhabitant(self, inhabitant):
        if inhabitant in self.inhabitants:
            self.inhabitants.remove(inhabitant)
