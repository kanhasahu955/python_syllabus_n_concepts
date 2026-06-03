"""Same method in parent and child class."""

class Employee:
    """instance method"""
    def calculate_salary(self):
        print("Calculating general employee salary")


class FullTimeEmployee(Employee):
    """instance method"""
    def calculate_salary(self):
        print("Salary = fixed monthly salary")


class ContractEmployee(Employee):
    """instance method"""
    def calculate_salary(self):
        print("Salary = hourly rate * working hours")


employees = [FullTimeEmployee(), ContractEmployee()]

for emp in employees:
    emp.calculate_salary()