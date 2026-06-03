"""instance method"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old')

person = Person('John', 20)
person.say_hello()

"""class method"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, name, age):
        return cls(name, age)

person = Person.from_string('John', 20)
print(person.name)
print(person.age)

"""static method"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def from_string(name, age):
        return Person(name, age)

person = Person.from_string('John', 20)
print(person.name)
print(person.age)

