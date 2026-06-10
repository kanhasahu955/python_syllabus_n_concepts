"""
Monkey patching is a technique that allows you to modify or extend the behavior of existing modules, classes, or functions at runtime without changing the original source code.

Applying monkey patching 
To apply the monkey patching technique, you follow these steps:

First, identify the target that can be a module, class, method, or function you want to patch.
Second, create your patch by writing code to add, modify, or replace existing logic.
Third, apply the patch by using an assignment to apply it to the target. The patch will overwrite or extend the existing behavior.

"""

def add_speach(cls):
    cls.speak = lambda self,message : print(f'{self.name} says: {message}')
    return cls


@add_speach
class Robot:
    def __init__(self,name):
        self.name = name



# Robot = add_speach(Robot)
robot = Robot('R2D2')
robot.speak('Hello, I am a robot')