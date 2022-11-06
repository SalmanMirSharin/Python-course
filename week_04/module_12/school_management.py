from re import X
from pyscreeze import grab


class School:
    #Constructor
    def __init__(self,school_name,address,principle='') -> None:
        self.school_name =school_name
        self.address = address
        self.princile = principle
        self.grades =[]

    def add_grade(self,name, teacher):
        new_grade = Grade(name, teacher)
        self.grades.append(new_grade)

    def remove_grade(self,name):
        idx =0
        for i, grade in enumerate(self.grades):
            if grade.name == name:
                idx =i
        del self.grades[idx]
 
class Grade:
    #Constructor
    def __init__(self,name,teacher) -> None:
        self.name = name
        self.student = []
        self.teacher = teacher

    def __repr__(self) -> str:
        return f'{self.name} with teacher {self.teacher}'

    # def __del__(self):
    #     print(f'Deletion {self.name} with teacher {self.teacher}')

oxford = School('Oxford kid Acadamy','uk','Jerin')
oxford.add_grade('Class-3','Osman gony')
oxford.add_grade('Class-5','Nazma mam')
oxford.add_grade('Class-8','Rajib sir')
print(oxford.grades)
oxford.remove_grade('Class-5')
print(oxford.grades)




        