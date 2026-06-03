"""
Abstraction means hiding internal implementation details and showing only the required functionality to the user.
Abstraction in Python OOP means hiding internal implementation details and exposing only essential features. 
In Python, we achieve abstraction using the abc module, ABC class, and @abstractmethod decorator. 
An abstract class cannot be instantiated directly. It is mainly used to define a common contract that child classes must follow.
"""


from abc import ABC, abstractmethod


# class PaymentProcessor(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass

# class CreditCardPayment(PaymentProcessor):
#     def pay(self, amount):
#         return f'Paid {amount} using credit card'

# class PayPalPayment(PaymentProcessor):
#     def pay(self, amount):
#         return f'Paid {amount} using PayPal'

# class BankTransferPayment(PaymentProcessor):
#     def pay(self, amount):
#         return f'Paid {amount} using bank transfer'


# payments = [CreditCardPayment(), PayPalPayment(), BankTransferPayment()]

# for payment in payments:
#     print(payment.pay(100))


from abc import ABC, abstractmethod


class Database(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass

    @abstractmethod
    def close(self):
        pass


class MySQLDatabase(Database):

    def connect(self):
        print("Connected to MySQL")

    def execute_query(self, query):
        print(f"Executing MySQL query: {query}")

    def close(self):
        print("MySQL connection closed")


class SnowflakeDatabase(Database):

    def connect(self):
        print("Connected to Snowflake")

    def execute_query(self, query):
        print(f"Executing Snowflake query: {query}")

    def close(self):
        print("Snowflake connection closed")


def run_report(db: Database):
    db.connect()
    db.execute_query("SELECT * FROM users")
    db.close()


mysql = MySQLDatabase()
snowflake = SnowflakeDatabase()

run_report(mysql)
run_report(snowflake)