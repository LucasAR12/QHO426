from abc import ABC, abstractmethod

class Tech(ABC):
    @abstractmethod
    def activate(self):
        pass

    @abstractmethod
    def deactivate(self):
        pass

class Alien(ABC):
    @abstractmethod
    def fire(self):
        pass

    @abstractmethod
    def fly(self):
        pass

class LaserTech(Tech):
    def activate(self):
        print("Laser activated.")

    def deactivate(self):
        print("Laser deactivated.")

class SpaceAlien(Alien):
    def fire(self):
        print("Alien firing weapons.")

    def fly(self):
        print("Alien flying.")
