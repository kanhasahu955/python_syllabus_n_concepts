"""
A child class should be able to replace its parent class without breaking the program.
"""

# Bad Example
class Bird:
    def fly(self):
        print("Bird is flying")


class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")


class Penguin(Bird):
    def fly(self):
        raise Exception("Penguin cannot fly")



# Good Example
class Bird:
    def eat(self):
        print("Bird is eating")


class FlyingBird(Bird):
    def fly(self):
        print("Bird is flying")


class Sparrow(FlyingBird):
    def fly(self):
        print("Sparrow is flying")


class Penguin(Bird):
    def swim(self):
        print("Penguin is swimming")


def make_bird_fly(bird: FlyingBird):
    bird.fly()


make_bird_fly(Sparrow())