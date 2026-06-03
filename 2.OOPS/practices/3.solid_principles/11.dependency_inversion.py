"""
High-level modules should not depend on low-level modules.
Both should depend on abstractions.
"""


# Bad Example
class MySQLDatabase:
    def save(self, data):
        print(f"Saved {data} to MySQL")


class UserService:
    def __init__(self):
        self.db = MySQLDatabase()

    def create_user(self, user):
        self.db.save(user)



# good example
from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass


class MySQLDatabase(Database):
    def save(self, data):
        print(f"Saved {data} to MySQL")


class MongoDatabase(Database):
    def save(self, data):
        print(f"Saved {data} to MongoDB")


class UserService:
    def __init__(self, db: Database):
        self.db = db

    def create_user(self, user):
        self.db.save(user)


mysql_db = MySQLDatabase()
user_service = UserService(mysql_db)

user_service.create_user({"name": "Rahul"})