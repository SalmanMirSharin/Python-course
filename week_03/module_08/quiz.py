# class Sales:
#     def __init__(self, id):
#         self.id = id
#         id = 100

# val = Sales(123)
# print (val.id)


#another:

# class People():
#     def __init__(self, name):
#       self.name = name

#     def namePrint(self):
#       print(self.name)

# person1 = People("Emma")
# person2 = People("Watson")
# person1.namePrint()

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# print(Dog('rufus',3))


class Person:
    def __init__(self, id):
        self.id = id

sam = Person(100)
sam.__dict__['age'] = 49
print (sam.age + len(sam.__dict__))