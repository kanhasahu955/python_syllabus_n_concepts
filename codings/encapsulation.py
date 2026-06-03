class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError('Salary cannot be negative')
        self.__salary = value

    
emp = Employee('John', 25, 5000)
print(emp.salary)
emp.salary = 2600000
print(emp.salary)