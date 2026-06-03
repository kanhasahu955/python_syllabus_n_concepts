# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         return f"{self.name} barks"

# class Cat(Animal):
#     def make_sound(self):
#         return f"{self.name} meows"

# dog = Dog("Buddy")
# print(dog.make_sound())

# cat = Cat("Whiskers")
# print(cat.make_sound())



"""single inheritance"""
class Person:
    """constructor method"""
    def __init__(self,name):
        self.name = name

    """instance method"""
    def greet(self):
        return f"Hello, {self.name}"



class Employee(Person):
    def __init__(self,name,age):
        # super().__init__(name)
        # super().__init__(name) is used to call the constructor of the parent class
        # self.name = name is used to assign the name to the employee object
        # self.age = age is used to assign the age to the employee object
        self.age = age
        self.name = name

    """instance method"""
    def greet(self):
        return f"Hi, it's {self.name}"


employee = Employee('John', 25)
print(employee.greet())
print(type(employee))
print(type(Employee))
print(isinstance(employee, Employee))

print(issubclass(Employee, Person))
print(issubclass(Person, Employee))

person = Person('Jane')
print(person.greet())