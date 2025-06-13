class Robot:
    MAX_ENERGY = 100
    laws = "Protect, Obey and Survive"

    @staticmethod
    def the_laws():
        print(Robot.laws)

    @classmethod
    def assemble(cls):
        return cls("Assembled Robot")

    def __init__(self, name="Robot", age=0):
        self.name = name
        self.age = age
        self.energy = 0

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f"Robot(name={self.name}, age={self.age}, energy={self.energy})"

    def __str__(self):
        return f"Robot {self.name} is {self.age} years old with energy {self.energy}."

    def grow(self):
        self.age += 1

    def eat(self, amount):
        self.energy = min(self.energy + amount, Robot.MAX_ENERGY)

    def move(self, distance):
        self.energy = max(self.energy - distance, 0)


if __name__ == "__main__":
    robot = Robot()
    robot.display()
