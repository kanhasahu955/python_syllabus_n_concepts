"""
LISKOV SUBSTITUTION PRINCIPLE

A child class should be able to replace the parent class without breaking the program

Liskov Substitution Principle means a child class should behave correctly when used in place of its parent class. 
It should not break expected parent behavior.
"""

class Bird:
    def fly(self):
        print("Bird is flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguin cannot fly")

# This breaks the rule because Penguin is a Bird, but it cannot fly.


class Bird:
    def eat(self):
        print("Bird is eating")

class FLyingBird(Bird):
    def fly(self):
        print("Bird is flying")


class Sparrow(FLyingBird):
    pass

class Penguin(Bird):
    pass

def make_bird_fly(bird: FLyingBird):
    bird.fly()

make_bird_fly(Sparrow())
make_bird_fly(Penguin())