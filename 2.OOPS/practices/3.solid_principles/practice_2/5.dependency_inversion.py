# dependency inversion principle
"""
High level modules should not depend on low level modules both should depend on abstractions.

Dependency Inversion Principle means classes should depend on abstraction, not concrete implementation. 
This makes code loosely coupled and easy to test or replace.
"""

class MySQLDatabase:
    def save_order(self,order):
        print(f"Saved {order} to MySQL")

class OrderService:
    def __init__(self):
        self.db = MySQLDatabase()

    def create_order(self,order):
        self.db.save_order(order)

order_service = OrderService()
order_service.create_order("Order 1")

"""
Problem

OrderService is tightly connected to MySQLDatabase.
Tomorrow, if you want to use PostgreSQL, MongoDB, or Supabase, you must change OrderService.

That is bad design.
"""

# Good Example
from abc import ABC, abstractmethod

class OrderRepository(ABC):
    @abstractmethod
    def save_order(self,order):
        pass

# Now create concrete implementations:
class MySQLOrderRepository(OrderRepository):
    def save_order(self,order):
        print(f"Saved {order} to MySQL")

class PostgreSQLOrderRepository(OrderRepository):
    def save_order(self,order):
        print(f"Saved {order} to PostgreSQL")

class MongoDBOrderRepository(OrderRepository):
    def save_order(self,order):
        print(f"Saved {order} to MongoDB")

class SupabaseOrderRepository(OrderRepository):
    def save_order(self,order):
        print(f"Saved {order} to Supabase")


# Now high-level service depends only on the abstraction:
class OrderService:
    def __init__(self,order_repository:OrderRepository):
        self.order_repository = order_repository

    def create_order(self,order):
        self.order_repository.save_order(order)

order_service = OrderService(MySQLOrderRepository())
order_service.create_order("Order 1")






class EmailService:
    def send_email(self, message):
        print(f"Email sent: {message}")


class UserService:
    def __init__(self):
        self.email_service = EmailService()

    def register_user(self, username):
        print(f"User registered: {username}")
        self.email_service.send_email("Welcome user")


from abc import ABC, abstractmethod


class NotificationService(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(NotificationService):

    def send(self, message):
        print(f"Email sent: {message}")


class SmsNotification(NotificationService):

    def send(self, message):
        print(f"SMS sent: {message}")


class PushNotification(NotificationService):

    def send(self, message):
        print(f"Push notification sent: {message}")


class UserService:

    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def register_user(self, username):
        print(f"User registered: {username}")
        self.notification_service.send("Welcome user")