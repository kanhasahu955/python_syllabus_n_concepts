from pprint import pprint

class Person:
    """class variables"""
    name = "Ashok Sahu"
    age = 20
    
    """instance method"""
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

    """class method"""
    @classmethod
    def change_name(cls,name):
        cls.name = name
    """class method"""
    @classmethod
    def change_age(cls,age):
        cls.age = age


print(Person.name)
print(Person.age)
Person.change_name("John Doe")
Person.change_age(30)
print(Person.name)
print(Person.age)

print(getattr(Person, 'name'))
print(getattr(Person, 'age'))

print(hasattr(Person, 'name'))
print(hasattr(Person, 'age'))

setattr(Person, 'name', 'kanha sahu')
setattr(Person, 'age', 31)

# delattr(Person, 'name')
# delattr(Person, 'age')

print(Person.name)
print(Person.age)

pprint(Person.__dict__)

# pprint(Person.__doc__)
# pprint(Person.__name__)
# pprint(Person.__module__)
# pprint(Person.__bases__)
# pprint(Person.__class__)
# pprint(Person.__dict__)
# pprint(Person.__doc__)
# pprint(Person.__name__)
# pprint(Person.__module__)
# pprint(Person.__bases__)
# pprint(Person.__class__)