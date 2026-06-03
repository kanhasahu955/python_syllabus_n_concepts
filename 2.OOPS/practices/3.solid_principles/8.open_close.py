"""
A class should be open for extension but closed for modification.

Meaning:
We should add new functionality without changing existing tested code.
"""

"""ABSTRACTION"""

from abc import ABC, abstractmethod

# Bad Example
class PaymentService:
    def pay(self, payment_type, amount):
        if payment_type == "credit_card":
            print(f"Paid {amount} using credit card")
        elif payment_type == "upi":
            print(f"Paid {amount} using UPI")
        elif payment_type == "net_banking":
            print(f"Paid {amount} using net banking")


payment_service = PaymentService()
payment_service.pay("credit_card", 100)
payment_service.pay("upi", 100)
payment_service.pay("net_banking", 100)


# Good Example
class PaymentService(ABC):

    @abstractmethod
    def pay(self,amount):
        pass

class CreditCardPayment(PaymentService):
    def pay(self,amount):
        print(f"Paid {amount} using credit card")

class UPIPayment(PaymentService):
    def pay(self,amount):
        print(f"Paid {amount} using UPI")

class NetBankingPayment(PaymentService):
    def pay(self,amount):
        print(f"Paid {amount} using net banking")

payments = [CreditCardPayment(), UPIPayment(), NetBankingPayment()]
for payment in payments:
    payment.pay(100)