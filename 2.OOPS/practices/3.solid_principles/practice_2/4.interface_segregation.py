# interface segregation principle
"""
A Class should not be forced to implement methods it does not need
do not create big interface with many methods, create small specific interfaces
"""

# Bad Example
from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class HumanWorker(Worker):
    def work(self):
        print("Human is working")

    def eat(self):
        print("Human is eating")


class RobotWorker(Worker):
    def work(self):
        print("Robot is working")

    def eat(self):
        raise Exception("Robot does not eat")

workers = [HumanWorker(),RobotWorker()]
for worker in workers:
    worker.work()
    worker.eat()

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

class HumanWorker(Workable,Eatable):
    def work(self):
        print("Human is working")
    
    def eat(self):
        print("Human is eating")

class RobotWorker(Workable):
    def work(self):
        print("Robot is working")



def start_work(worker: Workable):
    worker.work()

workers = [HumanWorker(),RobotWorker()]
for worker in workers:
    start_work(worker)
    worker.eat()