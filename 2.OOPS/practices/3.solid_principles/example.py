class NotificationService:
    def send(self, notification_type, message):
        if notification_type == "email":
            print(f"Sending email: {message}")
        elif notification_type == "sms":
            print(f"Sending SMS: {message}")
        elif notification_type == "whatsapp":
            print(f"Sending WhatsApp: {message}")



from abc import ABC, abstractmethod


class NotificationSender(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailSender(NotificationSender):
    def send(self, message):
        print(f"Sending email: {message}")


class SmsSender(NotificationSender):
    def send(self, message):
        print(f"Sending SMS: {message}")


class WhatsAppSender(NotificationSender):
    def send(self, message):
        print(f"Sending WhatsApp: {message}")


class NotificationService:
    def __init__(self, sender: NotificationSender):
        self.sender = sender

    def notify(self, message):
        self.sender.send(message)


email_service = NotificationService(EmailSender())
email_service.notify("Your order is confirmed")

sms_service = NotificationService(SmsSender())
sms_service.notify("Your OTP is 123456")



"""
SOLID PRINCIPLES
S - Single Responsibility Principle
O - Open/Closed Principle
L - Liskov Substitution Principle
I - Interface Segregation Principle
D - Dependency Inversion Principle



SOLID principles are five object-oriented design principles used to make software maintainable, 
scalable, and loosely coupled.

Single Responsibility means one class should have one reason to change. 
Open/Closed means code should be open for extension but closed for modification. 
Liskov Substitution means a child class should be replaceable wherever the parent class is used. 
Interface Segregation means a class should not be forced to implement unnecessary methods. 
Dependency Inversion means high-level classes should depend on abstractions, not concrete implementations.
"""

