from gc import collect, get_objects, disable
from ctypes import c_long

"""
In python 
A variable references an object that holds a value. In other words, variables are references.

To find the memory address of an object referenced by a variable, you pass the variable to the built-in id() function.

The id() function returns the memory address of an object referenced by a variable as a base-10 number.

To convert this memory address to a hexadecimal string, you use the hex() function:

To get the number of references of an object, you use the from_address() method of the ctypes module.

The Memory Manager destroys the object and reclaims the memory once the reference count of that object reaches zero.

when you have an object that references itself or two objects reference each other. This creates something called circular references.

When the Python Memory Manager cannot remove objects with circular references, it causes a memory leak.

This is why the garbage collector comes into play to fix the circular references.

Python automatically manages memory for you using reference counting and garbage collector.

Python garbage collector helps you avoid memory leaks by detecting circular references and destroy objects appropriately.


"""

def ref_address(address):
    return c_long.from_address(address).value

a = [1,2,3]
address_a = id(a)
print(ref_address(address_a))

b = a
print(ref_address(address_a))

a = None
print(ref_address(address_a))

b = None
print(ref_address(address_a))


def object_exists(address):
    for obj in get_objects():
        if id(obj) == address:
            return True
    return False


class A:
    def __init__(self):
        self.b = B(self)
        print(f'A: {hex(id(self))}, B: {hex(id(self.b))}')
class B:
    def __init__(self,a):
        self.a = a
        print(f'B: {hex(id(self))}, A: {hex(id(self.a))}')

disable()

a = A()
a_id = id(a)
b_id = id(a.b)

print(ref_address(a_id))
print(ref_address(b_id))

print(object_exists(a_id))
print(object_exists(b_id))


# run the garbage collector
collect()

# check if object exists
print(object_exists(a_id))
print(object_exists(b_id))

# check the reference count of the object
print(ref_address(a_id))
print(ref_address(b_id))

