# reverse number - done
# sum of number - done
# factorial of a number - done
# fibonacci series - done
# prime number - done


# reverse number 
def reverse_number(n:int)->int:
    if n <= 0:
        raise ValueError("Number must be positive")
    reversed_number = 0
    original_number = n
    while original_number > 0 :
        digit = original_number % 10
        reversed_number = reversed_number * 10 + digit
        original_number = original_number // 10
    return reversed_number

# prime numbers
def prime_numbers(n:int)->list[int]:
    if n <= 0 :
        raise ValueError("Number must be positive")
    prime_numbers = []

    def is_prime(number:int)->bool:
        if number <= 1:
            return False
        for i in range(2,number):
            if number % i == 0:
                return False
        return True
    for i in range(2,n):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers


# factorial of a number
def factorial(n:int)->int:
    if n < 0:
        raise ValueError("Number must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# fibonacci series
def fibonacci(n:int)->list[int]:
    if n <= 0:
        raise ValueError("Number must be positive")
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:   
        fibonacci_series = [0,1]
        for i in range(2,n):
            fibonacci_series.append(fibonacci_series[i-1] + fibonacci_series[i-2])
        return fibonacci_series


class Number:
    def __init__(self,number:int):
        self.number = number
    
    def reverse_number(self)->int:
        return reverse_number(self.number)
    def factorial(self)->int:
        return factorial(self.number)
    def fibonacci(self)->list[int]:
        return fibonacci(self.number)
    def prime_numbers(self)->list[int]:
        return prime_numbers(self.number)

number = Number(12)
print(f'Reverse number {number.number}: {number.reverse_number()}')
print(f'Factorial {number.number}: {number.factorial()}')
print(f'Fibonacci {number.number}: {number.fibonacci()}')
print(f'Prime numbers {number.number}: {number.prime_numbers()}')
