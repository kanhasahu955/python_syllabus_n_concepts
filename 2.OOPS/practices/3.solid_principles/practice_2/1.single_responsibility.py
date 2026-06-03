# single responsibility principle
"""
A class should have only one responsibility
only one class should be responsible for a single task
if a class has multiple responsibility we should split it into multiple classes
"""


# Bad Example
class UserService:
    def create_user(self,name,email):
        print(f"User {name} created")

    def send_mail(self,mail):
        print(f"Email sent to {mail}")

    def save_to_database(self,user):
        print("User saved to database")


user_service = UserService()
user_service.create_user("John","john@example.com")
user_service.send_mail("john@example.com")
user_service.save_to_database("John")

# Good Example

class UserService:
    def create_user(self,name,email):
        print(f"User {name} created")

class EmailService:
    def send_mail(self,mail):
        print(f"Email sent to {mail}")

class DatabaseService:
    def save_to_database(self,user):
        print("user saved to database")


user_service = UserService()
user_service.create_user("John","john@example.com")
email_service = EmailService()
email_service.send_mail("john@example.com")
database_service = DatabaseService()
database_service.save_to_database("john")