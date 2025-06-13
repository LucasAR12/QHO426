from human import Human
from robot import Robot

class Planet:
    def __init__(self, name):
        self.name = name
        self.inhabitants = {
            'humans': [],
            'robots': []
        }

    def add_human(self, human):
        if isinstance(human, Human):
            self.inhabitants['humans'].append(human)

    def remove_human(self, human):
        if human in self.inhabitants['humans']:
            self.inhabitants['humans'].remove(human)

    def add_robot(self, robot):
        if isinstance(robot, Robot):
            self.inhabitants['robots'].append(robot)

    def remove_robot(self, robot):
        if robot in self.inhabitants['robots']:
            self.inhabitants['robots'].remove(robot)

    def __repr__(self):
        return (f"Planet(name={self.name}, "
                f"humans={self.inhabitants['humans']}, "
                f"robots={self.inhabitants['robots']})")

    def __str__(self):
        humans_str = ", ".join([str(human) for human in self.inhabitants['humans']])
        robots_str = ", ".join([str(robot) for robot in self.inhabitants['robots']])
        return (f"Planet {self.name} with Humans: [{humans_str}] and Robots: [{robots_str}]")


if __name__ == "__main__":
    earth = Planet("Earth")
    h1 = Human(name="Alice", age=25)
    r1 = Robot(name="R2D2", age=10)
    earth.add_human(h1)
    earth.add_robot(r1)
    print(earth)
