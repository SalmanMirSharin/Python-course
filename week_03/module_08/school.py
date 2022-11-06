class Student:
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id


class Course:
    def __init__(self,name,teacher):
        self.name = name
        self.teacher = teacher


class Teacher:
    def __init__(self,name,course):
        self.name = name
        self.course =course

class School:
    def __init__(self,name,teacher,course,student):
        self.name = name
        self.teacher = teacher
        self.course = course
        self.student = student
        
    def get_student(self):
        for student in self.student:
            print(student.name)

school_name ='Phitron'
ds_course = Course('Data structure','Einstein')
teacher_1 = Teacher('Einstein',ds_course)
algo_course = Course('Algorithm','Edison')
teacher_2 = Teacher('Edison',algo_course)

student_1 = Student('Arman',19,45)
student_2 = Student('Alia Bhath',29,84)
student_3 = Student('Nidhi Agaral',30,69)

teachers =[teacher_1,teacher_2]
courses = [ds_course,algo_course]
students = [student_1,student_2,student_3]

my_school = School(school_name,teachers,courses,students)

print(my_school.course)

my_school.get_student()



