class Person:
    """constructor method"""
    def __init__(self,name,age):
        self.name = name
        self.age = age

    """instance method"""
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

    """instance method"""
    def set_name(self,name):
        self.name = name

    """instance method"""
    def set_age(self,age):
        self.age = age

    """instance method"""
    def get_name(self):
        return self.name

    """instance method"""
    def get_age(self):
        return self.age

person = Person("John Doe", 30)
print(person.get_details())
person.set_name("Jane Doe")
person.set_age(25)
print(person.get_details())
print(person.get_name())
print(person.get_age())