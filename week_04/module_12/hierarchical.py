from curses.ascii import EM
from pyautogui import position


class Employee:
    def __init__(self,name, id , salary , position):
        self.name = name
        self.id = id
        self.salary = salary
        self.position = position

class Developer(Employee):
    def __init__(self, name, id, salary, position,tech, focus):
       self.tech = tech
       self.area_of_work = focus
       super.__init__(name,id,salary,position)
       
class Testion(Employee):
    pass

class Sales(Employee):
    pass


class Techlead(Employee):
    def __init__(self,name,id,salary,position, team):
        self.team = team
        super().__init__(name,id,salary,position)
        

         