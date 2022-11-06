from abc import ABC,abstractmethod
#abstract base class:
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    @property
    def name(self):
        print('This is Name!')

    @abstractmethod
    def move(self):
        print('Moving around in the zoo!')

    
class Monkey(Animal):

    def __init__(self):
        self.__name = 'Monkey'

    def sing(self):
        print('Monkey is singling')
    
    def eat(self):
        print('Eating banana!')
    @property
    def move(self):
        print("we came in  the zoo!")
        super().move()
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value

layka = Monkey()
print(layka)
layka.eat()
#layka.move()
layka.name = 'Moonkey'
print(layka.name)