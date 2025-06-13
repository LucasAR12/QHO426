from Planet import Planet
from human import Human
from robot import Robot

class Universe:
    def __init__(self):
        self.planets = []

    def add_planet(self, planet):
        if planet not in self.planets:
            self.planets.append(planet)

    def show_populations(self):
        for planet in self.planets:
            num_humans = 0
            num_robots = 0
            for inhabitant in planet.inhabitants:
                if isinstance(inhabitant, Human):
                    num_humans += 1
                elif isinstance(inhabitant, Robot):
                    num_robots += 1
            print(f"Planet {planet.name} has {num_humans} humans and {num_robots} robots.")
