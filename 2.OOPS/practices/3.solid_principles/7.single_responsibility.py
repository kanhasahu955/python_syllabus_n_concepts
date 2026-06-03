"""
Single Responsibility Principle (SRP) states that a class should have only one responsibility.
It means that a class should have only one reason to change.
"""

# Bad Example
class UserService:
    def create_user(self, name, email):
        print(f"User {name} created")

    def send_email(self, email):
        print(f"Email sent to {email}")

    def save_to_database(self, user):
        print("User saved to database")

user_service = UserService()
user_service.create_user("John", "john@example.com")
user_service.send_email("john@example.com")
user_service.save_to_database("john@example.com")


# Good Example
class UserService:
    def create_user(self, name, email):
        print(f"User {name} created")
        return {"name": name, "email": email}


class EmailService:
    def send_email(self, email):
        print(f"Email sent to {email}")


class UserRepository:
    def save(self, user):
        print("User saved to database")

user_service = UserService()
user = user_service.create_user("John", "john@example.com")
email_service = EmailService()
email_service.send_email(user["email"])
user_repository = UserRepository()
user_repository.save(user)