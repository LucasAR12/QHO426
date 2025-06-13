import random
from planet import Planet
from human import Human
from robot import Robot
import matplotlib.pyplot as plt

class Universe:
    def __init__(self):
        self.planets = []

    def generate(self, planet_name):
        planet = Planet(planet_name)
        num_humans = random.randint(1, 5)
        num_robots = random.randint(1, 5)

        for _ in range(num_humans):
            planet.add_human(Human())

        for _ in range(num_robots):
            planet.add_robot(Robot())

        self.planets.append(planet)

    def show_populations(self, selection):
        planet_names = [planet.name for planet in self.planets]
        human_counts = [len(planet.inhabitants['humans']) for planet in self.planets]
        robot_counts = [len(planet.inhabitants['robots']) for planet in self.planets]
        total_counts = [human_counts[i] + robot_counts[i] for i in range(len(self.planets))]

        plt.figure(figsize=(10, 6))

        if selection == "human":
            plt.bar(planet_names, human_counts, color='blue')
            plt.title("Number of Humans per Planet")
            plt.ylabel("Humans")
        elif selection == "robot":
            plt.bar(planet_names, robot_counts, color='red')
            plt.title("Number of Robots per Planet")
            plt.ylabel("Robots")
        else:
            plt.bar(planet_names, total_counts, color='green')
            plt.title("Total Population per Planet")
            plt.ylabel("Population")

        plt.xlabel("Planets")
        plt.show()


if __name__ == "__main__":
    universe = Universe()
    universe.generate("Earth")
    universe.generate("Mars")
    universe.generate("Venus")

    universe.show_populations("human")
    universe.show_populations("robot")
    universe.show_populations("all")
