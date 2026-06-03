# class TemperatureConverter:
#     KEVIN = 'K',
#     FAHRENHEIT = 'F'
#     CELSIUS = 'C'

#     @staticmethod
#     def celsius_to_fahrenheit(c):
#         return 9*c/5 + 32

#     @staticmethod
#     def fahrenheit_to_celsius(f):
#         return 5*(f-32)/9

#     @staticmethod
#     def celsius_to_kelvin(c):
#         return c + 273.15

#     @staticmethod
#     def kelvin_to_celsius(k):
#         return k - 273.15

#     @staticmethod
#     def fahrenheit_to_kelvin(f):
#         return 5*(f+459.67)/9

#     @staticmethod
#     def kelvin_to_fahrenheit(k):
#         return 9*k/5 - 459.67

#     @staticmethod
#     def format(value, unit):
#         symbol = ''
#         if unit == TemperatureConverter.FAHRENHEIT:
#             symbol = '°F'
#         elif unit == TemperatureConverter.CELSIUS:
#             symbol = '°C'
#         elif unit == TemperatureConverter.KEVIN:
#             symbol = '°K'

#         return f'{value}{symbol}'


# print(TemperatureConverter.celsius_to_fahrenheit(100))
# print(TemperatureConverter.fahrenheit_to_celsius(100))
# print(TemperatureConverter.celsius_to_kelvin(100))
# print(TemperatureConverter.kelvin_to_celsius(100))
# print(TemperatureConverter.fahrenheit_to_kelvin(100))
# print(TemperatureConverter.kelvin_to_fahrenheit(100))
# print(TemperatureConverter.format(100, TemperatureConverter.FAHRENHEIT))
# print(TemperatureConverter.format(100, TemperatureConverter.CELSIUS))
# print(TemperatureConverter.format(100, TemperatureConverter.KEVIN))





class Calculator:
    @staticmethod
    def add(a,b):
        return a + b

    @staticmethod
    def subtract(a,b):
        return a - b

    @staticmethod
    def multiply(a,b):
        return a * b

    @staticmethod
    def divide(a,b):
        return a / b

    @staticmethod
    def modulus(a,b):
        return a % b

    @staticmethod
    def power(a,b):
        return a ** b

    @staticmethod
    def square(a):
        return a ** 2

    @staticmethod
    def cube(a):
        return a ** 3

    @staticmethod
    def square_root(a):
        return a ** 0.5

    @staticmethod   
    def is_even(a):
        return a % 2 == 0

    @staticmethod
    def is_odd(a):
        return a % 2 != 0

    @staticmethod
    def is_prime(a):
        if a <= 1:
            return False
        for i in range(2, a):
            if a % i == 0:
                return False
        return True

    @staticmethod
    def is_perfect(a):
        sum = 0
        for i in range(1, a):
            if a % i == 0:
                sum += i
        return sum == a
        

print(Calculator.add(10, 20))
print(Calculator.subtract(10, 20))
print(Calculator.multiply(10, 20))
print(Calculator.divide(10, 20))
print(Calculator.modulus(10, 20))
print(Calculator.power(10, 20))
print(Calculator.square(10))
print(Calculator.cube(10))
print(Calculator.square_root(10))
print(Calculator.is_even(10))
print(Calculator.is_odd(10))
print(Calculator.is_prime(10))
print(Calculator.is_perfect(10))