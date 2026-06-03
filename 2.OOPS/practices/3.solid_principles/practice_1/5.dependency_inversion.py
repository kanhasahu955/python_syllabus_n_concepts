"""
DEPENDENCY INVERSION PRINCIPLE

High-level modules should not depend on low-level modules.
Both should depend on abstractions.


Dependency Inversion Principle means classes should depend on abstraction, not concrete implementation. 
This makes code loosely coupled and easy to test or replace.
"""

class MySQLDatabase:
    def save(self, data):
        print(f"Saved {data} to MySQL")

class UserService:
    def __init__(self):
        self.db = MySQLDatabase()

    def create_user(self, user):
        self.db.save(user)

user_service = UserService()
user_service.create_user("John")

class Database:
    def save(self, data):
        pass


class MySQLDatabase(Database):
    def save(self, data):
        print("Saving data to MySQL:", data)


class MongoDatabase(Database):
    def save(self, data):
        print("Saving data to MongoDB:", data)


class UserService:
    def __init__(self, db: Database):
        self.db = db

    def create_user(self, name):
        self.db.save(name)