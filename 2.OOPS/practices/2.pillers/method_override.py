"""
Same method in parent and child class.
Method overriding in Python means redefining a parent class method inside the child class with the same method name. 
It allows the child class to provide its own implementation. 
It is used in inheritance and supports runtime polymorphism. 
If we want to call the parent class method inside the overridden method, we use super().
"""


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

# dog = Dog("Dog")
# print(dog.make_sound())

# cat = Cat("Cat")
# print(cat.make_sound())



# class Payment:
#     def pay(self,amount):
#         self.amount = amount

# class CreditCardPayment(Payment):
#     def pay(self,amount):
#         return f"Paid {amount} using credit card"

# class UPIPayment(Payment):
#     def pay(self,amount):
#         return f"Paid {amount} using UPI"

# class BankTransferPayment(Payment):
#     def pay(self,amount):
#         return f"Paid {amount} using bank transfer"

# payments = [CreditCardPayment(), UPIPayment(), BankTransferPayment()]
# for payment in payments:
#     print(payment.pay(100))



# class User:
#     def login(self):
#         print("User logged in")

# # class Admin(User):
# #     def login(self):
# #         print("Admin logged in")

# class Admin(User):
#     def login(self):
#         super().login()
#         print("Admin logged in with super method")

# user = User()
# admin = Admin()
# user.login()
# admin.login()



"""constructor overriding"""
class Person:
    """constructor method"""
    def __init__(self, name):
        self.name = name
        print("Person constructor called")


class Student(Person):
    """constructor method"""
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no
        print("Student constructor called")


student = Student("Rahul", 101)

print(student.name)
print(student.roll_no)