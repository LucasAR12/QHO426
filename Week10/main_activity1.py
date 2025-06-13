from human import Human
from robot import Robot

if __name__ == "__main__":
    human = Human("Lucas", 25, 80)
    print(repr(human))
    human.move(10)

    robot = Robot("R2-D2", 5, 90)
    print(repr(robot))
    robot.move(20)
    print(Robot.the_laws())
