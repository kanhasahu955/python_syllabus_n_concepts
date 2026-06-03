"""
Same method name with different parameters.
Python does not support traditional method overloading like Java.
"""

class Calculator:
    """instance method"""
    def add(self,a,b):
        return a + b

    """instance method"""
    def add(self,a,b,c):
        return a + b + c

calculator = Calculator()
print(calculator.add(10, 20))
print(calculator.add(10, 20, 30))