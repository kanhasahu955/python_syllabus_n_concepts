"""
A decorator is a function that takes another function and add extra behaviour to it and return a new function.

A decorator is a function that takes another function as an argument and extends its behaviour without changing the original function


Used for logging, authentication, authorization, caching, timing and more
"""

from functools import wraps

# --------------------------------  without arguments --------------------------------

# def logging(fn):
#     @wraps(fn)
#     def wrapper(*args,**kwargs):
#         result = fn(*args,**kwargs)
#         print(f'{fn.__name__} was called with {args} and {kwargs}')
#         return result
#     return wrapper


# @logging
# def add(a,b):
#     """ add two numbers and return the result
#     Arguments:
#         a: the first number
#         b: the second number
#     Return:
#         the sum of a and b
#     """
#     return a + b


# print(add(2,3))
# help(add)





# --------------------------------  with argumennts --------------------------------


# def repeat(times):
#     def decorator(fn):
#         @wraps(fn)
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 result = fn(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator



# @repeat(5)
# def print_log(message):
#     print(message)


# print_log('repeat hello')



# --------------------------------  class as decorator --------------------------------
class Star:
    def __init__(self, number_of_stars):
        self.n = number_of_stars

    def __call__(self,fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(self.n * "*")
            result = fn(*args, **kwargs)
            print(self.n * "*")
            return result
        return wrapper
    


@Star(5)
def add(a,b):
    return a + b


print(add(1,2))