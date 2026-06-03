"""
A class should not be forced to implement methods it does not need.
Python does not have interfaces like Java, but we can use abstract classes.
"""

from abc import ABC, abstractmethod

# Bad Example
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class HumanWorker(Worker):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")


class RobotWorker(Worker):
    def work(self):
        print("Robot working")

    def eat(self):
        raise Exception("Robot does not eat")



# Good Example
from abc import ABC, abstractmethod


class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class HumanWorker(Workable, Eatable):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")


class RobotWorker(Workable):
    def work(self):
        print("Robot working")