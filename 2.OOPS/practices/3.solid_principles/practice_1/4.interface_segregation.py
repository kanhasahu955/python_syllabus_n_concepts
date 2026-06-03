"""
INTERFACE SEGREGATION PRINCIPLE

A class should not be forced to implement methods it does not need

Interface Segregation Principle means we should create small, specific interfaces/classes 
instead of one large interface forcing unnecessary methods.
"""

class Worker:
    def work(self):
        print("Worker is working")
    
    def eat(self):
        print("Worker is eating")

class Robot(Worker):
    def work(self):
        print("Robot is working")

    def eat(self):
        raise Exception("Robot does not eat")

# Robot does not need eat() method, but it is forced to implement it.

# Good example
class Workable:
    def work(self):
        pass

class Eatable:
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

