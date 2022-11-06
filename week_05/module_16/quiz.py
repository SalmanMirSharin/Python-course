# Problem:
# class Test:
#     def __init__(self):
#         self.x = 0
# class Derived_Test(Test):
#     def __init__(self):
#         Test.__init__(self)
#         self.y = 1
# def main():
#     b = Derived_Test()
#     print(b.x,b.y)
# main()

#problem:

from abc import ABC, abstractmethod
class AbstractClass(ABC):
     @abstractmethod
     def some_method():
        pass
ac = AbstractClass()

print(ac)
