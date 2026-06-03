"""
MRO means Method Resolution Order.
It tells Python which class method should be executed first when multiple classes have the same method name.
"""

# class A:
#     def method(self):
#         print("A method")

# class B(A):
#     def method(self):
#         print("B method")

# class C(B):
#     def method(self):
#         print("C method")

# # c = C()
# # c.method()
# # print(C.__mro__)

# class D(A, B, C):
#     def method(self):
#         print("D method")

# d = D()
# # d.method()
# # print(D.__mro__)
# print(D.mro())


# class A:
#     def show(self):
#         print("A class")


# class B(A):
#     pass


# class C(A):
#     pass


# class D(B, C):
#     def show(self):
#         print("D method")


# obj = D()
# obj.show()

# print(D.mro())