from abc import ABC, abstractmethod

# class PaymentProcessor(ABC):
#     @abstractmethod
#     def pay(self,amoount):
#         pass

# class CreditCardPayment(PaymentProcessor):
#     def pay(self,amount):
#         return f'Paid {amount} using credit card'

# class UPIPayment(PaymentProcessor):
#     def pay(self,amount):
#         return f'Paid {amount} using UPI'

# class BankTransferPayment(PaymentProcessor):
#     def pay(self,amount):
#         return f'Paid {amount} using bank transfer'

# payments = [CreditCardPayment(), UPIPayment(), BankTransferPayment()]

# for payment in payments:
#     print(payment.pay(100))


class Database(ABC):
    """abstract method"""
    @abstractmethod
    def connect(self):
        pass
    """abstract method"""
    @abstractmethod
    def execute_query(self,query):
        pass
    """abstract method"""
    @abstractmethod
    def close(self):
        pass

class MySQLDatabase(Database):
    """instance method"""
    def connect(self):
        print("Connected to MySQL")
    """instance method"""
    def execute_query(self,query):
        print(f"Executing MySQL query: {query}")
    """instance method"""
    def close(self):
        print("MySQL connection closed")


class SnowflakeDatabase(Database):
    """instance method"""
    def connect(self):
        print("Connected to Snowflake")
    """instance method"""
    def execute_query(self,query):
        print(f"Executing Snowflake query: {query}")
    """instance method"""
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