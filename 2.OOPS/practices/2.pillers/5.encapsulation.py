class Employee:
    """constructor method"""
    def __init__(self,name,age,salary,address):
        self.name = name #public attribute
        self.age = age
        self.__salary = salary #private attribute
        self._age = age #protected attribute
        self.address = address #public attribute
        print('Initializing a new employee...')

    """property method"""
    @property
    def salary(self):
        print('Getting salary...')
        return self.__salary

    """property method"""
    @salary.setter
    def salary(self,value):
        if value < 0:
            raise ValueError('Salary cannot be negative')
        self.__salary = value

    @salary.deleter
    def salary(self):
        del self.__salary

    """instance method"""
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.__salary}"

emp = Employee('John', 25, 5000)
print(emp.salary)
emp.salary = 2600000
print(emp.salary)
print(emp.get_details())

