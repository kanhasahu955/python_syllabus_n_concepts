"""method overloading"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old')

person = Person('John', 20)
person.say_hello()
person.say_hello('Jane', 21) #method overloading
person.say_hello('Jane', 21, 'Python Developer') #method overriding


"""method overriding"""
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old')

employee = Employee('John', 20)
employee.say_hello()