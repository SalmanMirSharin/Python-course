# proble: 1:
# try:
#     if '1' != 1:
#         raise "someError"
#     else:
#         print("someError has not occurred")
# except "someError":
#     print ("someError has occurred")

# problem:2:
# f = open("text.txt",'r')
# f.readline()


# Problem 3:
# class A:
#     def __str__(self):
#         return '1'
# class B(A):
#     def __init__(self):
#         super().__init__()
# class C(B):
#     def __init__(self):
#         super().__init__()
# def main():
#     obj1 = B()
#     obj2 = A()
#     obj3 = C()
#     print(obj1, obj2,obj3)
# main()

# class A:
#     def __init__(self):
#         self.multiply(15)
#     def multiply(self, i):
#         self.i = 4 * i
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print(self.i)
 
#     def multiply(self, i):
#         self.i = 2 * i
# obj = B()


# Problem: 4
# # CODE 1
# @f
# def f1():
#         print('Hello')
# # CODE 2
# def f1():
#          print('Hello')
# f1 = f(f1)


# Problem: 6
# class A:
#     @staticmethod
#     def a(x):
#         print(x)
# A.a(100)


class Demo:
    def __check(self):
        return " Demo's check "
    def display(self):
        print(self.__check(),end="")
class Demo_Derived(Demo):
    def __check(self):
        return " Derived's check "
Demo().display()
Demo_Derived().display()

