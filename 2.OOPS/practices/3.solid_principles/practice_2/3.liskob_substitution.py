# liskov substitution principle
"""
A child class should be able to replace its parent class without breaking the program

we should be able to replace a parent class with a child class without breaking the program

Liskov Substitution Principle says that 
child classes should be replaceable with their parent class without breaking the application. 
A subclass should not remove or change the expected behavior of the parent class. 
If a child class cannot fully behave like the parent, then inheritance is probably wrong 
and we should redesign using separate abstractions.
"""

# Bad Example
class Bird:
    def fly(self):
        print("Bird is flying")

class Sparrow(Bird):
    def fly(self):
        print("sparrow is flying")

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguin cannot fly")

def make_bird_fly(bird:Bird):
    bird.fly()
    
make_bird_fly(Sparrow())
make_bird_fly(Penguin())


# Good Example
class Bird:
    def eat(self):
        print("Bird is eating")
    
class Sparrow(Bird):
    def eat(self):
        print("Sparrow is eating")
    
class Penguin(Bird):
    def eat(self):
        print("Penguin is eating")
    
def make_bird_eat(bird:Bird):
    bird.eat()

make_bird_eat(Sparrow())
make_bird_eat(Penguin())



class Payment:
    def pay(self,amount):
        print(f"Paid {amount} ")

class CreditCardPayment(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using credit card" )

class CashOnDeliveryPayment(Payment):
    def pay(self,amount):
        raise Exception("Cash on delivery is not support online payment")

def checkout(payment: Payment, amount):
    payment.pay(amount)


checkout(CreditCardPayment(), 1000)
checkout(CashOnDeliveryPayment(), 1000)



# Good Example
class OnlinePayment:
    def pay(self,amount):
        pass

class OfflinePayment:
    def pay(slef,amount):
        pass

class CreditCardPayment(OnlinePayment):
    def pay(self,amount):
        print(f"Paid {amount} using credit card")

class CashOnDeliveryPayment(OfflinePayment):
    def pay(self,amount):
        print(f"Paid {amount} using cash on delivery")

class UPIPayment(OnlinePayment):
    def pay(self,amount):
        print(f"Paid {amount} using UPI")


def checkout_online(payment:OnlinePayment,amount):
    payment.pay(amount)

def checkout_offline(payment:OfflinePayment,amount):
    payment.pay(amount)

checkout_online(CreditCardPayment(), 1000)
checkout_offline(CashOnDeliveryPayment(), 1000)
checkout_online(UPIPayment(), 1000)

