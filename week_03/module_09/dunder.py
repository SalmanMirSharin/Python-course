from unicodedata import name


class Person:
    def __init__(self,name,age,money,height=65):
        self.name = name
        self.age = age
        self.money = money
        self.height = height

    def __add__(self,other):
        return self.money + other.money
    
    def __call__(self):
        print( f'This is {self.name} with age {self.age} and have money {self.money}')
    
    def __eq__(self, other):
        if self.age == other.age:
            return True
        return False
    
    def __len__(self):
        return self.height

alim = Person('Alim',15,530)
dalim = Person('Dalim',16,660)

#print(alim+dalim)

# print(alim==dalim)

print()