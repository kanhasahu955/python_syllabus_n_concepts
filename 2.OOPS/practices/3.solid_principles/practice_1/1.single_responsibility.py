"""
SINGLE RESPONSIBILITY PRINCIPLE

A class should have only one responsibility
only one class should do one job only, if a class has multiple responsibility, we should split it into multiple classes
"""

# Bad Example
class UserService:
    def create_user(self, name, email):
        print(f"User {name} created")

    def send_email(self, email):
        print(f"Email sent to {email}")


user_service = UserService()
user_service.create_user("John", "john@example.com")
user_service.send_email("john@example.com")


# Good Example
class UserService:
    def create_user(self, name, email):
        print(f"User {name} created")
        return {"name": name, "email": email}

class EmailService:
    def send_email(self, email):
        print(f"Email sent to {email}")



user_service = UserService()
user = user_service.create_user("John", "john@example.com")
email_service = EmailService()
email_service.send_email(user["email"])
