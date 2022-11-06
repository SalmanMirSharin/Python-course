#other problem:
# class Dog:
#     def walk(self):
#         return "*walking*"
#     def speak(self):
#         return "Woof!"
    
# class JackRussellTerrier(Dog):
#      def talk(self):
#          return super().speak()

# bobo = JackRussellTerrier()
# print(bobo.talk())

#other problem:
# class Dog:
#     def walk(self):
#         return "*walking*"
#     def speak(self):
#         return "Woof!"
# class JackRussellTerrier(Dog):
#      def speak(self):
#          return "Arff!"
# bobo = JackRussellTerrier()
# print(bobo.speak())

#other problem:

from numpy import percentile


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self) -> str:
        return f'{self.name} and age is {self.age}'

P = Person("Habib",13)
print(P)